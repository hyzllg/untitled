import time
import pyautogui
import random



for i in range(1,28):

    pyautogui.click(x=random.randint(800, 830),y=random.randint(460, 480), duration=0.5)
    time.sleep(28)
    pyautogui.click(x=random.randint(580, 800),y=random.randint(420, 520), duration=0.5)
    pyautogui.click(x=random.randint(580, 800),y=random.randint(950, 1000), duration=0.5)

    pyautogui.click(x=random.randint(580, 800),y=random.randint(420, 520), duration=0.8)
    pyautogui.click(x=random.randint(580, 800),y=random.randint(950, 1020), duration=0.8)

    time.sleep(1)
    pyautogui.click(x=random.randint(580, 800),y=random.randint(420, 520), duration=0.8)
    pyautogui.click(x=random.randint(580, 800),y=random.randint(950, 1000), duration=0.8)
    # a = random.randint(9,21)
    time.sleep(1)

    print("第{}次！".format(i))
