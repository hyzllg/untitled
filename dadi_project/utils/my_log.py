import logging
import os
import time


# class Log:
#     def __init__(self):
#         self.log = logging.getLogger()
#         self.log.setLevel(level="DEBUG")
#     def get_formatter(self):
#         console_fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#         file_fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#         return console_fmt,file_fmt
#     def console_handler(self):
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(level="INFO")
#         console_handler.setFormatter(self.get_formatter()[0])
#         return console_handler
#     def file_handler(self):
#         file_handler = logging.FileHandler('./log.txt',mode='a',encoding='utf-8')
#         file_handler.setLevel(level="INFO")
#         file_handler.setFormatter(self.get_formatter()[1])
#         return file_handler
#     def get_log(self):
#         self.log.addHandler(self.console_handler())
#         self.log.addHandler(self.file_handler())
#     def debug(self,message):
#         self.log.debug(message)
#     def info(self,message):
#         self.log.info(message)
#         self.log.removeHandler(self.console_handler())
#         self.log.removeHandler(self.file_handler())
#     def warning(self,message):
#         self.log.warning(message)
#     def error(self,message):
#         self.log.error(message)
#     def critical(self,message):
#         self.log.critical(message)

class Log():
    #log日志模块
    def __init__(self):
        # log_path是日志存放路径地址
        get_path = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(os.path.dirname(get_path), "log")

        # 如果不存在这个logs文件夹，就自动创建一个
        if not os.path.exists(log_path): os.mkdir(log_path)
        # 文件的命名
        self.logname = os.path.join(log_path,"%s.log"%time.strftime("%Y-%m-%d"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')

    def __console(self,level,message):

    # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname,"a",encoding='utf-8') # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self,message):
        self.__console("debug",message)
    def info(self,message):
        self.__console("info",message)
    def warning(self,message):
        self.__console("warning",message)
    def error(self,message):
        self.__console("error",message)
