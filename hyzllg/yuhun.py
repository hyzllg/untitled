import random
import time

import pyautogui


def yuhun(h):
    n = 0
    while n<h:

        pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        time.sleep(27)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(940, 1000), duration=0.6)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(2000, 2050), duration=0.6)
        time.sleep(random.randint(5, 10) / 10)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(940, 1000), duration=0.6)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(2000, 2050), duration=0.6)
        time.sleep(random.randint(1, 5) / 10)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(940, 1000), duration=0.6)
        pyautogui.click(x=random.randint(1250, 1700), y=random.randint(2000, 2050), duration=0.6)
        time.sleep(random.randint(15, 20) / 10)
        n+=1
        print(f'第{n}次！')

if __name__ == '__main__':
    yuhun(120)