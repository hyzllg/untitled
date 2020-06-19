#!/bin/env python
''' This code is mainly used to test the board's performance '''
import os
import posixpath #路径处理库
import time
import logging  #日志
import shutil   #拷贝文件
import unittest  #单元测试框架
import threading  #线程
import wave    #读写WAV文件
import audioop #模块包含对声音片段的一些有用操作
import soundfile

import pyaudio
from pocketsphinx import AudioFile

from adb_wrapper.adb_auto import AdbAuto, AdbFailException, AdbConnectFail

LOG_FOLDER = os.path.join(os.path.dirname(__file__), u'log')
LOG_FMT = logging.Formatter('%(asctime)s %(levelname)-8s [%(funcName)s:%(lineno)d] %(message)s')
LOG_LEVEL = logging.DEBUG

device = '123456789abcde'
ANDROID_SERIAL = os.getenv(u'ANDROID_SERIAL')
WORKSPACE = "/tmp/test"

ARECORD_PARAMS = {
    u'card_num': 'plug:echo_ref',
    u'samplerate': 48000,
    u'format': u'S32_LE',
    u'channels': 2,
}
stream = u'example.wav'
noise_stream = u'noise.wav'
test_words = [
    u'go', u'forward', u'spectacular',
    u'marvelous', u'congratulation',
    u'carefully', u'negative',
    u'nationality', u'beautiful', u'universally'
]
pass_threshold = 5 # 5/10, detect over 5 words treat as pass alexa disgusting

class RecordThread(threading.Thread):
    def __init__(self, audiofile='arecord.wav'):
        threading.Thread.__init__(self)
        self.bRecord = True
        self.audiofile = audiofile
        self.chunk = 1024
        self.format = pyaudio.paInt32
        self.channels = 2
        self.rate = 48000

    def run(self):
        audio = pyaudio.PyAudio()
        wavfile = wave.open(self.audiofile, 'wb')
        wavfile.setnchannels(self.channels)
        wavfile.setsampwidth(audio.get_sample_size(self.format))
        wavfile.setframerate(self.rate)
        wavstream = audio.open(format=self.format,
                               channels=self.channels,
                               rate=self.rate,
                               input=True,
                               frames_per_buffer=self.chunk)
        while self.bRecord:
            wavfile.writeframes(wavstream.read(self.chunk))
        wavstream.stop_stream()
        wavstream.close()
        audio.terminate()

    def stoprecord(self):
        self.bRecord = False

class ArecordTest(unittest.TestCase):
    ''' Audio recognition '''
    @classmethod
    def setUpClass(cls):
        if os.path.isdir(LOG_FOLDER):
            shutil.rmtree(LOG_FOLDER)
        os.makedirs(LOG_FOLDER)
        logging.getLogger().setLevel(logging.INFO)

        main_conhdl = logging.StreamHandler()
        main_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'main.log'))
        main_loghdl.setFormatter(LOG_FMT)
        main_conhdl.setFormatter(LOG_FMT)
        main_loghdl.setLevel(LOG_LEVEL)
        cls.logger = logging.getLogger('main')
        cls.logger.addHandler(main_loghdl)
        cls.logger.addHandler(main_conhdl)

        case_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'suite.log'))
        case_loghdl.setLevel(LOG_LEVEL)
        cls.suite_logger = logging.getLogger('suite')
        cls.suite_logger.addHandler(case_loghdl)

        adb_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'adb.log'))
        adb_loghdl.setFormatter(LOG_FMT)
        adb_loghdl.setLevel(LOG_LEVEL)
        adb_logger = logging.getLogger('adb')
        adb_logger.addHandler(adb_loghdl)
        cls.adb = AdbAuto(logger=adb_logger)
        # cls.adb.device = ANDROID_SERIAL
        cls.adb.device = cls.adb.connect_auto(device)

    @classmethod
    def tearDownClass(cls):
        del cls.adb
        del cls.logger

    def setUp(self):
        self.logger.info('Try adb connect/root')
        self.suite_logger.info("[STEP] adb connection/root")
        for _ in range(30):
            try:
                self.adb.connect_auto()
                self.adb.root_auto()
            except (AdbFailException, AdbConnectFail):
                time.sleep(1)
                continue
            break
        else:
            self.logger.error("Adb Fail to connect")
            raise RuntimeError('Adb Fail to connect')
        self.suite_logger.info("[STEP] Create Folder %s", WORKSPACE)
        self.adb.shell('mkdir -p {}'.format(WORKSPACE))

    def push_stream(self, stream):
        '''push stream to board'''
        stream_path = os.path.join(os.path.dirname(__file__), u'streams', stream)
        if not os.path.isfile(stream_path):
            self.logger.error('Fail to find stream: %s', stream_path)
            raise RuntimeError('No Stream Exist')
        self.suite_logger.info("[STEP] Push %s to %s", stream_path, WORKSPACE)
        try:
            self.adb.push_auto(stream_path, WORKSPACE, timeout=180)
            self.adb.shell('sync')
            self.logger.info('Push stream successful')
        except AdbFailException as err:
            self.logger.error('Push Stream Fail: %s', err)
            raise RuntimeError('Push Stream Fail')

    def audio_recognize(self, pcm_file):
        '''audio recognize reliable data'''
        file4sphinx = pcm2sphinx(pcm_file)
        audio = AudioFile(audio_file=file4sphinx)
        recognize_words = []
        for phrase in audio:
            for s in phrase.seg():
                recognize_words.append(s.word)
        return recognize_words

    def recognize_assert(self, pcm_filename):
        '''pocketsphinx comparison of results'''
        recognize_words = self.audio_recognize(os.path.join(LOG_FOLDER, pcm_filename))
        hints = 0
        for word in test_words:
            for statement in recognize_words:
                if word in statement:
                    self.logger.info("Found Word: %s/%s", word, statement)
                    hints += 1
                    break
        if hints < pass_threshold:
            self.logger.error("Too less word recognize: %s/%s", hints, len(test_words))
        self.assertGreaterEqual(hints, pass_threshold, "Too less word recognize")

    def template_record(self, playback, file_name, paramD =False):
        remote_wav_path = WORKSPACE + '/' + file_name
        if paramD:
            arecord_cmd = arecord_cmd_gen(ARECORD_PARAMS, file_name, paramD=True)
        else:
            arecord_cmd = arecord_cmd_gen(ARECORD_PARAMS, file_name)
        self.logger.info("Record Command: %s", arecord_cmd)
        res, adb_arecord = self.adb.shell_unblock(arecord_cmd)
        if not res:
            self.logger.error("Record Command Fail")
            self.logger.debug("stdout: %s", adb_arecord.stdout.read())
            self.logger.debug("stderr: %s", adb_arecord.stderr.read())
            raise RuntimeError("Record Command Start Fail")
        self.logger.info("Record Start")
        playback()
        if adb_arecord.isalive():
            time.sleep(5)
            self.logger.info(u"Stop Record Command")
            adb_arecord.kill()
        self.adb.shell_auto(u'sync')
        self.logger.info(u"Record Complete")
        try:
            self.adb.pull_auto(remote_wav_path, LOG_FOLDER, timeout=300)
            self.logger.info('adb pull complete')
        except AdbFailException as err:
            self.logger.error("Pull tinycap record file fail: %s", err)
            raise RuntimeError("Pull tinycap record file fail")
        self.recognize_assert(file_name)

    def record_stream(self, playback):
        '''The audio recording'''
        temp_file = os.path.splitext(stream)[0] + u'format.wav'
        audio_record = RecordThread(os.path.join(LOG_FOLDER, temp_file))
        self.logger.info("* start recording")
        audio_record.start()
        time.sleep(3)
        playback()
        time.sleep(3)
        self.logger.info("* done recording")
        audio_record.stoprecord()
        self.adb.shell('sync')
        return temp_file

    def test_aplay(self):
        def playback():
            self.logger.info('push stream to board')
            self.push_stream(stream)
            self.logger.info('aplay the stream')
            self.adb.shell('aplay {}'.format(posixpath.join(WORKSPACE, stream)))
        pcm_filename = self.record_stream(playback)
        self.recognize_assert(pcm_filename)

    # def test_arecord_mic(self):
    #     ''''''
    #     def playback():
    #         self.logger.info("Start Playback: %s", stream)
    #         play_stream(os.path.join(os.path.dirname(__file__), u'streams', stream))
    #         self.logger.info("Playback Done")
    #     self.template_record(playback, 'mic.wav')
    #
    # def test_arecord_ref(self, ):
    #     self.push_stream(stream)
    #     def playback():
    #         self.logger.info("Start Playback: %s", stream)
    #         res, adb_shell = self.adb.shell_unblock('aplay {}'.format(posixpath.join(WORKSPACE, stream)))
    #         play_stream(os.path.join(os.path.dirname(__file__), u'streams', noise_stream))
    #         for _ in range(5):
    #             if adb_shell.isalive():
    #                 time.sleep(1)
    #                 continue
    #         else:
    #             adb_shell.kill()
    #             self.logger.info('Has killed pid\n')
    #         self.logger.info("Playback Done")
    #     self.template_record(playback, 'ref.wav', paramD=True)

def play_stream(wav_path):
    '''Input wav file path, send to playback from system'''
    chunk = 1024
    datas = []
    audio_format = None
    audio_channels = None
    audio_rate = None
    audio = pyaudio.PyAudio()
    try:
        with open(wav_path, 'rb') as wav_f:
            try:
                wav = wave.open(wav_f)
                audio_format = audio.get_format_from_width(wav.getsampwidth())
                audio_channels = wav.getnchannels()
                audio_rate = wav.getframerate()
                data = wav.readframes(chunk)
                while len(data) > 0:
                    datas.append(data)
                    data = wav.readframes(chunk)
            except wave.Error as err:
                raise RuntimeError("Read Wav Fail: {}".format(err))
    except IOError as err:
        raise RuntimeError("Open Wav Fail: {}".format(err))
    if not datas:
        raise RuntimeError("Wav Read Blank Content")
    stream = audio.open(format=audio_format, channels=audio_channels,
                          rate=audio_rate, output=True)
    for data in datas:
        try:
            stream.write(data)
        except IOError:
            pass
    stream.stop_stream()
    stream.close()
    audio.terminate()

def arecord_cmd_gen(record_params, file_name, paramD=False):
    stringparams ={
        u'card_num': u'D'
    }
    string2params = {
        u'samplerate': u'r',
        u'format': u'f',
        u'channels': u'c',
    }
    cmds = [u'arecord']
    if paramD:
        string2params.update(stringparams)
        for key, value in record_params.items():
            param = string2params.get(key)
            if param:
                cmds.append(u'-{} {}'.format(param, value))
        cmds.append('{}'.format(os.path.join(WORKSPACE, file_name)))
    else:
        for key, value in record_params.items():
            param = string2params.get(key)
            if param:
                cmds.append(u'-{} {}'.format(param, value))
        cmds.append('{}'.format(os.path.join(WORKSPACE, file_name)))
    return u' '.join(cmds)

def pcm2sphinx(wav_file):
    '''Convert file to wav'''
    # Convert PCM to 16bit 16khz mono for pocketsphinx
    def bitdepth2sampwidth(bitdepth):
        # sampwidth for python wave param
        return bitdepth / 8
    def bitdepth2subtype(bitdepth):
        # subtype for soundfile param subtype
        return {
            8: u'PCM_U8',
            16: u'PCM_16',
            24: u'PCM_24',
            32: u'PCM_32',
        }[bitdepth]

    sphinx_channels = 1
    sphinx_samplerate = 16000
    sphinx_bitdepth = 16

    prefix = os.path.splitext(os.path.basename(wav_file))[0]
    wav_to_16bit_filename = os.path.join(LOG_FOLDER, prefix+u'.{}bit.wav'.format(sphinx_bitdepth))
    audio_data, _ = soundfile.read(wav_file)
    soundfile.write(wav_to_16bit_filename, audio_data, 48000, subtype=bitdepth2subtype(sphinx_bitdepth))

    wav_to_sphinx_filename = os.path.join(LOG_FOLDER, prefix+u'.sphinx.wav')
    wavfile = wave.open(wav_to_16bit_filename, 'rb')
    audio_data = wavfile.readframes(wavfile.getnframes())
    wavfile.close()

    # WAV Samplerate -> 16khz
    frames = audioop.ratecv(
        audio_data, bitdepth2sampwidth(sphinx_bitdepth),
        2, 48000, sphinx_samplerate, None)

    # WAV Channels -> Mono Channel
    if sphinx_channels == 1:
        frames = audioop.tomono(frames[0], bitdepth2sampwidth(sphinx_bitdepth), 0.5, 0.5)

    wavfile = wave.open(wav_to_sphinx_filename, 'wb')
    wavfile.setparams((
        sphinx_channels, bitdepth2sampwidth(sphinx_bitdepth), sphinx_samplerate,
        0, 'NONE', 'Uncompressed'))
    wavfile.writeframes(frames)
    wavfile.close()

    return wav_to_sphinx_filename

if __name__ == '__main__':
    unittest.main()

