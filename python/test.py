import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="",
    database="whatsapp-add"
)
cursor = db.cursor()

# cursor.execute("SELECT phone_no FROM submit_form WHERE id ")


# cursor.execute("SELECT FROM submit_form")

# result = cursor.fetchall()
# phoneNumbers = str(result)[3:-4]
# print(phoneNumbers)
# mycursor = db.cursor()

sql = "SELECT phone_no FROM submit_form submit_form WHERE id"

cursor.execute(sql)

result = cursor.fetchall()
# print(phoneNumbers)
for x in result:
  phoneNum = x
  phoneNum = str(x)[2:-3]
  print(phoneNum)

# import webbrowser

# webbrowser.open('https://web.whatsapp.com/send?phone=+94775667922&text=itworked')