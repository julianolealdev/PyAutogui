#screen of a notebook, changes can be needed if you are in a desktop

import pyautogui
with pyautogui.hold('alt'):
    pyautogui.press('tab')
with pyautogui.hold('ctrl'):
    pyautogui.press('t')
with pyautogui.hold('fn'):
    pyautogui.press('f4')
pyautogui.write('https://www.youtube.com/')
pyautogui.press('enter')
pyautogui.sleep(5)
pyautogui.click(1000,120)
pyautogui.write('The Beatles Eleanor Rigby')
pyautogui.press('enter')
pyautogui.sleep(2)                      
pyautogui.click(600,300)