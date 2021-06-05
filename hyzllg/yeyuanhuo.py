import random
import time

import pyautogui


def yuhun(h):
    n = 0
    while n<h:

        pyautogui.click(x=random.randint(1550,1650), y=random.randint(920,980),duration=0.6)
        time.sleep(20)
        pyautogui.click(x=random.randint(1550,1650), y=random.randint(920,980), duration=0.6)
        time.sleep(random.randint(1, 5) / 10)
        pyautogui.click(x=random.randint(1550,1650), y=random.randint(920,980), duration=0.6)
        time.sleep(random.randint(1, 5) / 10)
        pyautogui.click(x=random.randint(1550,1650), y=random.randint(920,980), duration=0.6)
        time.sleep(random.randint(1, 5) / 10)
        pyautogui.click(x=random.randint(1550,1650), y=random.randint(920,980), duration=0.6)
        time.sleep(random.randint(1, 5) / 10)
        pyautogui.click(x=random.randint(1550,1650), y=random.randint(920,980), duration=0.6)
        time.sleep(random.randint(1, 5) / 10)

        n+=1
        print(f'第{n}次！')

if __name__ == '__main__':
    yuhun(150)