import webbrowser
import pyautogui
import time
from datetime import datetime,timedelta
import clipboard
import mysql.connector
from tkinter import *

root = Tk()

# database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="",
    database="whatsapp-add"
)
cursor = db.cursor()
sql = "SELECT phone_no FROM submit_form submit_form WHERE id"
cursor.execute(sql)
result = cursor.fetchall()

# gui def
def startbtn():
  grpName = grpNameinpt.get()
  root.destroy()

  # open whatsapp web
  webbrowser.open('https://web.whatsapp.com/')

  time.sleep(20)
  # print(pyautogui.position())

  # search group
  pyautogui.click(457,266)
  pyautogui.typewrite(grpName)

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

  # get invite link from clipboard
  msg = clipboard.paste()

  time.sleep(2)

  # go to whatsapp profile with msg
  for x in result:
      phoneNum = x
      phoneNum = str(x)[2:-3]
      print(phoneNum)
      pyautogui.click(256,51)
      pyautogui.typewrite("https://web.whatsapp.com/send?phone="+phoneNum+"&text="+msg)
      pyautogui.press('enter')

      time.sleep(10)

      pyautogui.click(1287,1009)
      pyautogui.press('enter')

      time.sleep(5)

# GUI
root.title("Whatsapp Groups Add")
width = 496
height = 200
root.geometry("%dx%d" % (width, height))
root.resizable(False,False)

lf = LabelFrame(root, text="What is your group name? ", font=('arial bold', 18))
lf.pack(pady=10)

grpNameinpt = Entry(lf, font=('Helvetica', 24))
grpNameinpt.pack(pady=5, padx=20)

statBtn = Button(lf, text="Start", command=startbtn, font=('Arial', 12), padx=5, pady=5)
statBtn.pack(pady=10)

root.mainloop()
