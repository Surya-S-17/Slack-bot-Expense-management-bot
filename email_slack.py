import smtplib

email="yyyyyyyy@gmail.com"
receive="xxxxxxx@gmail.com"

def send_email(emp_id,string):
    subject= f"EXPENSE REPORT {emp_id}"
    message= string

    text = f"Subject: {subject}\n\n{message}"
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(email,"pass")

    server.sendmail(email,receive,text)

    print("sent")

