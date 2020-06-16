import logging
import time
from logging import handlers

# logging.debug('debug message')     #调试
# logging.info('info message')       #信息
# logging.warning('warning message') #警告
# logging.error('error message')     #错误
# logging.critical('critical message')#批判性
# filename = r'C:\Users\16621\Desktop\logging.log'
# fh = logging.FileHandler(filename,encoding='utf-8')
# sh = logging.StreamHandler()
#
# logging.debug('debug message')     #调试
# logging.info('info message')       #信息
# logging.warning("warning message test")
# logging.error("error message test")
# logging.critical("critical message test")


rh = handlers.RotatingFileHandler('myapp.log',maxBytes=1024,backupCount=5)
fh = handlers.TimedRotatingFileHandler(filename='x2.log',when='s',interval=5,encoding='utf-8')
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s[line : %(lineno)d] - %(module)s : %(message)s',
    datefmt="%Y-%m-%d %H:%M:S %p",
    # handlers=[fh,sh],
    level=logging.DEBUG,
    handlers=[fh,rh]
)
for i in range(1,10000):
    time.sleep(1)
    logging.error('KeyboardInterrupt error %s'%str(i))




