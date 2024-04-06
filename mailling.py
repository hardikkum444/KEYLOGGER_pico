import smtplib
from email.mime.text import MIMEText
import os

def sendMail(subject, message, to_email):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 #this is the new port which allows for starttls based encryption instead of 25 son!
    smtp_user = 'your email'
    smtp_password = 'gmail app pass'


    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error --> {e}")

    # try:
    #     os.remove("mailing.py")
    # except Exception as e:
    #     print(f"{e}")


if __name__ == "__main__":
    subject = 'this is a test'
    message = "hello this is also a test!"
    to_email = 'recievers emailID'

    sendMail(subject, message, to_email)
