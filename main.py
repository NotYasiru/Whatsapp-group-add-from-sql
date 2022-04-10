import webbrowser
import pyautogui
import time
import pywhatkit

# open whatsapp web
webbrowser.open('https://web.whatsapp.com/')

time.sleep(15)
# print(pyautogui.position())

# search group
pyautogui.click(457,266)
pyautogui.typewrite("texting")

time.sleep(1)

# select group
pyautogui.click(458,371)

time.sleep(1)

# go to group settings
pyautogui.click(1116,123)

time.sleep(1)

# scroll down
pyautogui.click(1591,471)
pyautogui.hscroll(-1000)

time.sleep(1)

# click on invite link btn
pyautogui.click(1414,767)

time.sleep(1)

#copy link
pyautogui.click(1449,425)

time.sleep(1)