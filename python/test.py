# import mysql.connector

# db = mysql.connector.connect(
    # host = "localhost",
    # user = "root",
    # password="",
    # database="whatsapp-add"
# )
# cursor = db.cursor()

# cursor.execute("SELECT phone_no FROM submit_form WHERE id ")


# cursor.execute("SELECT FROM submit_form")

# result = cursor.fetchall()
# phoneNumbers = str(result)[3:-4]
# print(phoneNumbers)
# mycursor = db.cursor()

# sql = "SELECT phone_no FROM submit_form submit_form WHERE id"

# cursor.execute(sql)

# result = cursor.fetchall()
# print(phoneNumbers)
# for x in result:
#   phoneNum = x
#   phoneNum = str(x)[2:-3]
#   print(phoneNum)

# import webbrowser

# webbrowser.open('https://web.whatsapp.com/send?phone=+94775667922&text=itworked')


# from tkinter import *
# root = Tk()

# root.title("Whatsapp Groups Add")
# width = 496
# height = 200
# root.geometry("%dx%d" % (width, height))
# root.resizable(False,False)

# lf = LabelFrame(root, text="What is your group name? ", font=('arial bold', 18))
# lf.pack(pady=10)

# grpNameinpt = Entry(lf, font=('Helvetica', 24))
# grpNameinpt.pack(pady=5, padx=20)

# def startbtn():
  # grpName = grpNameinpt.get()
  # print(grpName)
  # root.destroy()

# gen_pwd = Button(lf, text="Start", command=startbtn, font=('Arial', 12), padx=5, pady=5)
# gen_pwd.pack(pady=10)

# root.mainloop()
