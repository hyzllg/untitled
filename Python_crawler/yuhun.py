import random
import time
import win32api,win32con
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
        time.sleep(random.randint(15, 20) / 10)

        n+=1
        print(f'第{n}次！')

def yeyuanhuo(h):
    n = 0
    while n<h:
        start = time.time()
        pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        time.sleep(38)
        pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        # pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        time.sleep(random.randint(5, 10) / 10)
        pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        # pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        time.sleep(random.randint(1, 5) / 10)
        pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        # pyautogui.click(x=random.randint(1630,1690), y=random.randint(900,960),duration=0.6)
        time.sleep(random.randint(15, 20) / 10)
        n+=1
        end = time.time()
        print(f"运行时间：{end-start}")

        print(f'第{n}次！')
# def yuhun(number,lists):
#     n = 0
#     while n<number:
#         pyautogui.click(x=random.randint(lists[0]+8,lists[1]-8), y=random.randint(lists[4]+8,lists[5]-8),duration=0.6)
#         time.sleep(27)
#         pyautogui.click(x=random.randint(lists[2]+50, lists[3]-50), y=random.randint(lists[6]+10, lists[7]-10), duration=0.6)
#         pyautogui.click(x=random.randint(lists[2]+50, lists[3]-50), y=random.randint(lists[8]+10, lists[9]-10), duration=0.6)
#         time.sleep(random.randint(5, 10) / 10)
#         pyautogui.click(x=random.randint(lists[2]+50, lists[3]-50), y=random.randint(lists[6]+10, lists[7]-10), duration=0.6)
#         pyautogui.click(x=random.randint(lists[2]+50, lists[3]-50), y=random.randint(lists[8]+10, lists[9]-10), duration=0.6)
#         time.sleep(random.randint(1, 5) / 10)
#         pyautogui.click(x=random.randint(lists[2]+50, lists[3]-50), y=random.randint(lists[6]+10, lists[7]-10), duration=0.6)
#         pyautogui.click(x=random.randint(lists[2]+50, lists[3]-50), y=random.randint(lists[8]+10, lists[9]-10), duration=0.6)
#         time.sleep(random.randint(15, 20) / 10)
#         n+=1
#         print(f'第{n}次！')

# def main(number):
#     lists = []
#     x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
#     y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
#     yin_y = int(y/23*22/2)
#     yin_x = int(x/2)
#     hx = int(yin_x/2)
#     hy = int(yin_y/9)
#     lists.append(int(yin_x/32*30))
#     lists.append(int(yin_x/32*31))
#     lists.append(hx)
#     lists.append(yin_x)
#     lists.append(int(yin_y/15*13))
#     lists.append(int(yin_y/15*14))
#     lists.append(hy*8)
#     lists.append(yin_y)
#     lists.append(yin_y+hy*8)
#     lists.append(yin_y*2)
#     yuhun(number,lists)

if __name__ == '__main__':
    # main(70)
    yuhun(150)
    # yeyuanhuo(50)


