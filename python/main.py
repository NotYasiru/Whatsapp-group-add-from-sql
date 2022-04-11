import webbrowser
import pyautogui
import time
import pywhatkit
from datetime import datetime,timedelta
import clipboard


phoneNumber = "+94775667922"

# open whatsapp web
webbrowser.open('https://web.whatsapp.com/')

time.sleep(20)
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


# get time after 1min
now = datetime.now()
now_plus_1 = now + timedelta(minutes = 1)
now_plusH = int(now_plus_1.strftime("%H"))
now_plusM = int(now_plus_1.strftime("%M"))

# get invite link from clipboard
msg = clipboard.paste()

# go to whatsapp profile with msg
pyautogui.click(256,51)
pyautogui.typewrite("https://web.whatsapp.com/send?phone=+94775667922&text=itworkedUsingpyAutoGUI")
pyautogui.press('enter') 

time.sleep(10)

# send msg
pyautogui.click(1287,1009)
pyautogui.press('enter')