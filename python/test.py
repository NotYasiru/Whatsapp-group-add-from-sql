import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="",
    database="whatsapp-add"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT phone_no FROM submit_form")

myresult = mycursor.fetchall()
str(myresult)[3:-4]

# mycursor = db.cursor()


# import webbrowser

# webbrowser.open('https://web.whatsapp.com/send?phone=+94775667922&text=itworked')