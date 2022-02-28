import pyautogui
import random
from time import sleep

# 默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止
pyautogui.FAILSAFE =False


def yongshengzhihai(number):
    for i in range(number):
        pyautogui.click(random.randint(1510,1580),random.randint(880,940),duration=0.6)
        sleep(42)
        for a in range(6):
            pyautogui.click(random.randint(1510, 1580), random.randint(880, 940), duration=0.8)


if __name__ == '__main__':
    yongshengzhihai(30)