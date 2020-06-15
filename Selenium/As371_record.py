#!/bin/env python
''' This code is mainly used to test the board's performance '''
import os
import time
import sys
import logging
import shutil
import unittest
import threading
import wave
import subprocess
import audioop
import pyaudio
import soundfile
from parameterized import parameterized
import sounddevice as sd

from pocketsphinx import AudioFile
from adb_wrapper.adb_auto import AdbAuto, AdbFailException, AdbConnectFail

LOG_FOLDER = os.path.join(os.path.dirname(__file__), u'log')
LOG_FMT = logging.Formatter('%(asctime)s %(levelname)-8s [%(funcName)s:%(lineno)d] %(message)s')
LOG_LEVEL = logging.DEBUG

device = '12345678'
FILEPATH = "/data/local/tmp/"
test_words = [u'go', u'forward', u'spectacular', u'disgusting', u'congratulation', u'carefully', u'negative', u'nationality', u'beautiful', u'alexa']
pass_threshold = 5 # 3/5, detect over 3 words treat as pass

class RecordThread(threading.Thread):
    def __init__(self, audiofile=None):
        threading.Thread.__init__(self)
        self.bRecord = True
        self.audiofile = audiofile
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000

    def run(self):

        audio = pyaudio.PyAudio()
        # print(sd.query_devices())
        # print("----------------------record device list---------------------")
        #
        # info = audio.get_host_api_info_by_index(0)
        # numdevices = info.get('deviceCount')
        # for i in range(0, numdevices):
        #     if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        #         print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))
        #
        # print("-------------------------------------------------------------")
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

class As371_6ch(unittest.TestCase):
    ''' Audio recognition '''
    @classmethod
    def setUpClass(cls):
        if os.path.isdir(LOG_FOLDER):
            shutil.rmtree(LOG_FOLDER)
        os.makedirs(LOG_FOLDER)
        logging.getLogger().setLevel(logging.INFO)

        adb_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'adb.log'))
        adb_loghdl.setFormatter(LOG_FMT)
        adb_loghdl.setLevel(LOG_LEVEL)
        adb_logger = logging.getLogger('adb')
        adb_logger.addHandler(adb_loghdl)
        main_conhdl = logging.StreamHandler()
        main_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'main.log'))
        main_loghdl.setFormatter(LOG_FMT)
        main_conhdl.setFormatter(LOG_FMT)
        main_loghdl.setLevel(LOG_LEVEL)
        cls.logger = logging.getLogger('main')
        cls.logger.addHandler(main_loghdl)
        cls.logger.addHandler(main_conhdl)

        cls.adb = AdbAuto(logger=adb_logger)
        cls.adb.device = cls.adb.connect_auto(device)

    @classmethod
    def tearDownClass(cls):
        del cls.adb
        del cls.logger

    def setUp(self):
        self.logger.info('root Platform')
        time.sleep(5)
        for _ in range(30):
            try:
                self.adb.connect_auto()
                self.adb.root_auto()
            except (AdbFailException, AdbConnectFail):
                time.sleep(1)
                continue
            self.logger.info("System Boot Complete")
            break
        else:
            self.logger.error("System Fail to Boot Complete")
        if os.path.isdir(FILEPATH):
            shutil.rmtree(FILEPATH)
            raise RuntimeError("System Fail to Boot Complete")
        self.adb.shell('mkdir -p {}'.format(FILEPATH))

    def push_file(self, stream):
        try:
            self.adb.push_auto(stream, FILEPATH, device, timeout=180)
            self.logger.info('push file successful')
        except RuntimeError:
            self.logger.warning('push file fail')

    def record_stream(self, stream):
        temp_file = os.path.splitext(stream)[0] + u'format.wav'
        audio_record = RecordThread(os.path.join(LOG_FOLDER, temp_file))
        time.sleep(3)
        self.logger.info("* start recording")
        audio_record.start()
        time.sleep(3)
        res, adb_shell = self.adb.shell_unblock("slesTest_playFdPath {} 0".format(os.path.join(FILEPATH, stream)))
        for _ in range(60):
            if adb_shell.isalive():
                time.sleep(1)
                continue
            break
        self.logger.info("* done recording")
        audio_record.stoprecord()
        self.adb.shell('sync')
        return temp_file

    def recognize_assert(self, stream):
        '''pocketsphinx comparison of results'''

        self.push_file(stream)
        temp_file = self.record_stream(stream)
        recognize_words = audio_recognize(os.path.join(LOG_FOLDER, temp_file))
        hints = 0
        for word in test_words:
            for statement in recognize_words:
                if word in statement:
                    self.logger.info("Found Word: %s/%s", word, statement)
                    hints += 1
                    break
        if hints < pass_threshold:
            self.logger.error("Too less words recognize: %s/%s", hints, len(test_words))
        self.assertGreaterEqual(hints, pass_threshold, "Too less word recognized")

    @parameterized.expand([u'2222.wav'])
    def test_As371_analyze_record(self, stream):
        self.logger.info('start test the {}'.format(stream))
        self.recognize_assert(stream)

def audio_recognize(pcm_file):
    '''audio recognize reliable data'''

    config = {
        'audio_file': pcm_file
    }
    audio = AudioFile(**config)
    recognize_words = []
    for phrase in audio:
        for s in phrase.seg():
            recognize_words.append(s.word)
    return recognize_words


def audio_conv_wav(pcm_file):
    '''Convert file to wav'''
    sphinx_channels = 1
    sphinx_samplerate = 16000

    s_read = wave.open(pcm_file, 'rb')
    format_file = os.path.splitext(pcm_file)[0] + u'format.wav'
    s_write = wave.open(format_file, 'wb')
    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)
    try:
        converted = audioop.ratecv(data, 2, 2, 44100, sphinx_samplerate, None)
        if sphinx_channels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
        s_write.setparams((sphinx_channels, 2, sphinx_samplerate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except TypeError as e:
        logging.warning('this is a issue:%s' % e)
    s_read.close()
    s_write.close()
    sys.stdout.write('File type conversion successful\n')
    return format_file

if __name__ == '__main__':
    unittest.main()