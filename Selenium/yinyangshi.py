import pyautogui
import time
import random
n = 0
while n<100:

    pyautogui.click(x=random.randint(890,920), y=random.randint(510,530),duration=0.6)
    time.sleep(28)
    pyautogui.click(x=random.randint(880, 940), y=random.randint(490, 510), duration=0.6)
    pyautogui.click(x=random.randint(1820, 1880), y=random.randint(490, 510), duration=0.6)
    time.sleep(random.randint(5, 10) / 10)
    pyautogui.click(x=random.randint(880, 940), y=random.randint(490, 510), duration=0.6)
    pyautogui.click(x=random.randint(1820, 1880), y=random.randint(490, 510), duration=0.6)
    time.sleep(random.randint(1, 5) / 10)
    pyautogui.click(x=random.randint(880, 940), y=random.randint(490, 510), duration=0.6)
    pyautogui.click(x=random.randint(1820, 1880), y=random.randint(490, 510), duration=0.6)
    time.sleep(random.randint(15, 20) / 10)
    n+=1
    print(f'第{n}次！')


