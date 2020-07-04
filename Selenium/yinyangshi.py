import pyautogui
import time
import random
n = 0
while n<100:

    pyautogui.click(x=random.randint(810,840), y=random.randint(970,1000),duration=0.5)
    time.sleep(28)
    pyautogui.click(x=random.randint(500, 840), y=random.randint(470, 510), duration=0.5)
    pyautogui.click(x=random.randint(500, 840), y=random.randint(995, 1030), duration=0.5)
    time.sleep(random.randint(5, 10) / 10)
    pyautogui.click(x=random.randint(500, 840), y=random.randint(470, 510), duration=0.5)
    pyautogui.click(x=random.randint(500, 840), y=random.randint(995, 1030), duration=0.5)
    time.sleep(random.randint(1, 5) / 10)
    pyautogui.click(x=random.randint(500, 840), y=random.randint(470, 510), duration=0.5)
    pyautogui.click(x=random.randint(500, 840), y=random.randint(995, 1030), duration=0.5)
    time.sleep(random.randint(10, 15) / 10)
    n+=1
    print(f'第{n}次！')


