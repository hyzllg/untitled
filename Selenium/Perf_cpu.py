import os
import re
import logging
import shutil
import time
from collections import defaultdict

from Test_Cases_addon.PM import pm_init
from Test_Cases_addon.PM.basepm import PMException
from adb_wrapper.adb_auto import AdbAuto, AdbFailException

SERIAL_PORT = os.getenv(u'SERIAL_PORT')
LOG_FOLDER = os.path.join(os.path.dirname(__file__), u'log')
LOG_FMT = logging.Formatter('%(asctime)s %(levelname)-8s [%(funcName)s:%(lineno)d] %(message)s')
LOG_LEVEL = logging.DEBUG

# PM_IP = os.getenv(u'NETBOOTER_IP')
# PM_OUTLET = os.getenv(u'OUTLET')
PM_IP = '10.70.56.68'
PM_OUTLET = 1
DEFAULT_ACCOUNT = u'admin'
DEFAULT_PASSWORD = u'admin'
COUNT = 5
VERSION = '1.0'
ANDROID_SERIAL = os.getenv(u'ANDROID_SERIAL')
device = '123456789ABCDEF'
CASE_COMMAND = {
    'CASE1': {'ampclient_samples 2 -O 3 ': 'HEVC_Main@L5_3840x2160p24_8bit4k60.ts'},
    'CASE2': {'ampclient_samples 2 -O 3 ': 'bbb_short.fmpeg.1920x1080.mp4.libx265_6500kbps_30fps.libfaac_stereo_128kbps_48000hz2k60.mp4'}
}
REMOTE_ARTIFACTS_FOLDER = u'/data/local/tmp'

class ADB_TIMEOUT(Exception):
    pass

class CpuUsageRate(object):
    ''' Do AwakenTime Test '''
    result = None
    def __init__(self, name='get_cpu_usage_rate'):
        self.name = name
        if os.path.isdir(LOG_FOLDER):
            shutil.rmtree(LOG_FOLDER)
        os.makedirs(LOG_FOLDER)
        logging.getLogger().setLevel(logging.DEBUG)

        main_conhdl = logging.StreamHandler()
        main_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'main.log'))
        main_loghdl.setFormatter(LOG_FMT)
        main_loghdl.setLevel(logging.INFO)
        main_conhdl.setFormatter(LOG_FMT)
        main_loghdl.setLevel(LOG_LEVEL)
        self.logger = logging.getLogger('main')
        self.logger.addHandler(main_loghdl)
        self.logger.addHandler(main_conhdl)

        case_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'suite.log'))
        case_loghdl.setFormatter(LOG_FMT)
        case_loghdl.setLevel(LOG_LEVEL)
        self.suite_logger = logging.getLogger('suite')
        self.suite_logger.addHandler(case_loghdl)

        adb_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'adb.log'))
        adb_loghdl.setFormatter(LOG_FMT)
        adb_loghdl.setLevel(LOG_LEVEL)
        adb_logger = logging.getLogger('adb')
        adb_logger.addHandler(adb_loghdl)

        self.logger.info("PM IP: %s", PM_IP)
        pm_loghdl = logging.FileHandler(os.path.join(LOG_FOLDER, u'pm.log'))
        pm_loghdl.setFormatter(LOG_FMT)
        pm_loghdl.setLevel(LOG_LEVEL)
        pm_logger = logging.getLogger('pm')
        pm_logger.addHandler(pm_loghdl)
        self.has_pm = False
        try:
            self.pm = pm_init(link=PM_IP, logger=logging)
            self.logger.info("Init PM Success")
            self.has_pm = True
        except PMException as e:
            self.logger.error('debug: %s', e)
            self.logger.warning("Init PM Fail")

        self.adb = AdbAuto(logger=adb_logger)
        #self.adb.device = ANDROID_SERIAL
        self.adb.device = self.adb.connect_auto(device)

    def ac_cycle(self):
        '''Restart the board'''
        if self.has_pm:
            self.logger.info("AC Off")
            self.pm.off(PM_OUTLET)
            time.sleep(10)
        if self.has_pm:
            self.logger.info("AC On")
            self.pm.on(PM_OUTLET)

    def check_boot_up(self):
        self.ac_cycle()
        self.suite_logger.info("[CHECKPOINT] Android Boot Complete by getprop dev.bootcomplete")
        time.sleep(7)
        for _ in range(30):
            try:
                cmd_info, _ = self.adb.shell_auto(u'getprop dev.bootcomplete')
                if cmd_info == u'1':
                    self.logger.info("Android Boot Complete")
                    break
            except AdbFailException:
                self.logger.warning("Android Not Boot")
            time.sleep(1)
        else:
            self.logger.error("Android Fail to Boot Complete")
            raise RuntimeError("Android Fail to Boot Complete")

    def play_stream(self, commands):
        for command, stream in commands.items():
            try:
                self.adb.root_auto()
                self.adb.push_auto(os.path.join(os.path.dirname(__file__), stream), REMOTE_ARTIFACTS_FOLDER, timeout=300)
                self.adb.shell_auto(u'sync')
            except AdbFailException as err:
                raise RuntimeError("push stream file fail: %s", err)
            remote_file_path = REMOTE_ARTIFACTS_FOLDER + u'/' + stream
            self.adb.shell(command + remote_file_path)
            self.logger.info('stream play complete')

    def adb_cmd_check(self, cmd, retry, timeout=15):
        i = 1
        while i <= retry:
            try:
                cmd_info, cmd_stderr = self.adb.shell(cmd, timeout=timeout)
            except AdbFailException:
                self.logger.warning("adb cmd: %s run failed , %s times retry" % (cmd, str(i)))
                i = i + 1
                time.sleep(1)
                continue
            else:
                self.logger.info('====adb cmd: %s run successfully====', cmd)
                break
        else:
            self.logger.error('Exceed max time ro run cmd: %s', cmd)
            raise ADB_TIMEOUT('ADB shell cmd run failed')
        return cmd_info, cmd_stderr

    def perf_cpu_usage_rate(self):
        all_data = defaultdict(list)
        VG4_RE = re.compile(r'G\s*?([A-Z]*?)\s*?\(')
        cpu_cmd = 'cat /proc/stat | head -1'
        stream_status_cmd = 'cat /proc/cpm/status |grep V4G'
        def get_cpu_data(status):
            for _ in range(10):
                stream_play_status, _ = self.adb_cmd_check(stream_status_cmd, 5)
                VG4_status = VG4_RE.findall(stream_play_status)
                if VG4_status[0] == status:
                    self.logger.info('VG4 status is: %s', VG4_status[0])
                    play_info, _ = self.adb_cmd_check(cpu_cmd, 1)
                    data = play_info.split()[1:]
                    break
                time.sleep(1)
                continue
            else:
                self.logger.error('Exceed max time')
                raise RuntimeError('Data acquisition failed')
            return data
        def processing_data(datas):
            float_data = []
            for data in datas:
                float_data.append(float(data))
            return float_data
        for category, commands in CASE_COMMAND.items():
            #self.check_boot_up()
            category = category + ' Unit(%)'
            for _ in range(COUNT):
                stream_play_info, _ = self.adb_cmd_check(cpu_cmd, 1)
                self.play_stream(commands)
                start_data = stream_play_info.split()[1:]
                end_data = get_cpu_data('OFF')

                process_start_data = processing_data(start_data)
                process_stop_data = processing_data(end_data)
                total = sum(process_stop_data) - sum(process_start_data)
                idle = process_stop_data[3] - process_start_data[3]
                pcpu = (total - idle) / total
                all_data[category].append(pcpu)
            time.sleep(2)
        return all_data

    def grep_data(self, grep_list):
        data_list = []
        for cpu_data in grep_list:
            if cpu_data == None:
                data_list.append(',None')
            else:
                data_list.append(',' + str(int(cpu_data * 100)))
        if None not in grep_list:
            data_list.append(','+str(int(max(grep_list)*100))+','+str(int(min(grep_list)*100))+','+str(
                int(((sum(i for i in grep_list))/COUNT)*100))+'\n')
        else:
            new_data = []
            count = 0
            for data in grep_list:
                if data != None:
                    new_data.append(data)
                    count += 1
                else:
                    continue
            if count:
                data_list.append(','+str(int(max(new_data)*100))+','+str(int(min(new_data)*100))+','+str(
                int(((sum(i for i in new_data))/COUNT)*100))+'\n')
            else:
                data_list.append(',None'*3+'\n')
        return data_list

def main():
    ''' The main run method is used to write to the file '''
    rate = CpuUsageRate()
    data_list = []
    data_list.append(u'Test Case,' + rate.name + '\n')
    data_list.append(u'Tools Version,' + VERSION + '\n')
    data_list.append(u'Category')
    for i in range(1, COUNT + 1):
        data_list.append(u',Round{}'.format(i))
    data_list.append(u',MAX,MIN,AVG' + '\n')
    all_data = rate.perf_cpu_usage_rate()
    for suite_name, data in all_data.items():
        data_list.append(suite_name)
        need_data = rate.grep_data(data)
        data_list.extend(need_data)
    data = ''.join(data_list)
    with open('Result.csv', 'ab') as file:
        file.write(data.encode('UTF-8'))

if __name__ == '__main__':
    main()

