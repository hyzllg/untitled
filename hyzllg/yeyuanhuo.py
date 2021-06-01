import random
import time

import pyautogui


def yuhun(h):
    n = 0
    while n<h:

        pyautogui.click(x=random.randint(1530,1590), y=random.randint(900,960),duration=0.6)
        time.sleep(35)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(940, 1000), duration=0.6)
        time.sleep(random.randint(5, 10) / 10)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(940, 1000), duration=0.6)
        time.sleep(random.randint(5, 10) / 10)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(940, 1000), duration=0.6)
        time.sleep(random.randint(5, 10) / 10)
        print(f'第{n}次！')

if __name__ == '__main__':
    yuhun(100)