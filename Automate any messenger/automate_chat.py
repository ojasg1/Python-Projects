import pyautogui
import time


text = 'I love Python!'

counter = 3

while counter>0:
    time.sleep(3)
    pyautogui.typewrite(text)


    time.sleep(10)
    pyautogui.press('enter')
    counter -= 1
