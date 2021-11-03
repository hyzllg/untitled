import yaml
import os
import selenium
import cx_Oracle
from utils import database_manipulation
import logging



'''
第一步：
    创建日志器
        logger = logging.getloger()
第二步：
    创建处理器
        console_handler = logging.StreamHandler()
第三步：
    设置格式器
        


'''
# #创建日志器对象
# logger = logging.getLogger()
# logger.setLevel(level="DEBUG")
# #定义处理器
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('./log.txt',mode='a',encoding='utf-8')
# #定义格式器
# console_fmt = "%(asctime)s %(name)s %(levelname)s"
# file_fmt = "%(name)s %(levelname)s %(asctime)s"
# fmt1 = logging.Formatter(fmt=console_fmt)
# fmt2 = logging.Formatter(fmt=file_fmt)
# console_handler.setFormatter(fmt1)
# file_handler.setFormatter(fmt2)
# console_handler.setLevel(level="ERROR")
# file_handler.setLevel(level="ERROR")
# #日志器添加处理器
# logger.addHandler(console_handler)
# # logger.addHandler(file_handler)


class Log:
    def __init__(self):
        self.log = logging.getLogger()
        self.log.setLevel(level="DEBUG")
    def get_formatter(self):
        console_fmt = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s")
        file_fmt = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s")
        return console_fmt,file_fmt
    def console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level="ERROR")
        console_handler.setFormatter(self.get_formatter()[0])
        return console_handler
    def file_handler(self):
        file_handler = logging.FileHandler('./log.txt',mode='a',encoding='utf-8')
        file_handler.setLevel(level="ERROR")
        file_handler.setFormatter(self.get_formatter()[1])
        return file_handler
    def get_log(self):
        self.log.addHandler(self.console_handler())
        self.log.addHandler(self.file_handler())
    def debug(self,message):
        self.log.debug(message)
    def info(self,message):
        self.log.info(message)
    def warning(self,message):
        self.log.warning(message)
    def error(self,message):
        self.log.error(message)
    def critical(self,message):
        self.log.critical(message)




log = Log()
logger = log.get_log()
log.debug("这是debug信息")
log.info("这是info信息")
log.warning("这是warning信息")
log.error("这是error信息")
log.critical("这是critical信息")
