import time
import random

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def bankcard():
    a = str(random.randint(1000, 10000))
    b = time.strftime("%m%d%H%M%S")
    bankcard = '621466' + b
    return bankcard
