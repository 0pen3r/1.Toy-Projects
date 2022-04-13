import pyautogui
import time
import datetime
import keyboard

"""
use pyautogui

pip install pyautogui
"""


# safe mode
# pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def pymacro():
    pyautogui.alert('엔터 후, 3초 안에 마우스 이동')
    time.sleep(3)
    address = pyautogui.position()

    # pyautogui.alert(pyautogui.position(), "Your Address", "START = Enter")
    step1 = pyautogui.confirm(text=address, title="Your MOuse Address",
                              buttons=["START"])

    step2 = pyautogui.prompt(text="Time?", title="How",
                             default='몇분동안 진행?')

    # 검증1
    print("몇분 : ", step2)
    asis = datetime.datetime.now()
    # 검증1

    i = 0
    while i < int(step2):
        time.sleep(5)
        pyautogui.click(address, button='left', clicks=5, interval=11)
        i = i+1

        if keyboard.is_pressed("F7"):
            pyautogui.alert("eeeeeeeeeeee")
            pyautogui.moveTo(0, 0)
            break

        # 검증2
        print("click %d" % i)
        print("end")
        # 검증2

    # 검증3
    tobe = datetime.datetime.now()
    print(asis, tobe)
    # 검증3


j = 0
# macro start
while j < 1:
    print('시작')
    pymacro()
    j = j+1
    # 검증4
