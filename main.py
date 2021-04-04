import webbrowser
import keyboard
import time
import pyautogui
import sys

if __name__ == '__main__':
    whil = 0
    while whil == 0:
        time.sleep(0.7)
        keyboard.press('t')
        time.sleep(0.1)
        pyautogui.write('/dupe')
        keyboard.press('enter')
        time.sleep(0.1)
        keyboard.press('2')
        time.sleep(0.1)
        keyboard.press('q')
        time.sleep(0.1)
        keyboard.press('1')
        if keyboard.is_pressed('end'):
            exit()