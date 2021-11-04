import yaml
import os
import selenium
import cx_Oracle
from utils import database_manipulation,Log
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
    fmt = logging.Formatter()
#第四步：
    日志器添加处理器
    logger.addHandler()
        


'''
# #创建日志器对象
# logger = logging.getLogger()
# logger.setLevel(level="DEBUG")
# #定义处理器
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('./log.txt',mode='a',encoding='utf-8')
# #定义格式器
# console_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# file_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# fmt1 = logging.Formatter(fmt=console_fmt)
# fmt2 = logging.Formatter(fmt=file_fmt)
# console_handler.setFormatter(fmt1)
# file_handler.setFormatter(fmt2)
# console_handler.setLevel(level="ERROR")
# file_handler.setLevel(level="ERROR")
# #日志器添加处理器
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
#
# logger.error("这是debug信息")

conn = cx_Oracle.connect()
cursor = conn.cursor()
cursor.execute()
