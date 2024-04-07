import smtplib
from email.mime.text import MIMEText
import os

def sendMail(subject,to_email):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'hardikkumawat444@gmail.com'
    smtp_password = 'bpjl gqyw yhpm sdpy'

    try:
        with open("loggings.txt", "r") as f:
            content = f.read()

    except Exception as e:
        print(f"Error reading file --> {e}")


    msg = MIMEText(content)
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


# if __name__ == "__main__":
#     subject = 'this is a test'
#     message = "hello this is also a test!"
#     to_email = 'hardikkumawat444@gmail.com'
#     # to_email = 'ashishpathak823@gmail.com'

#     sendMail(subject,to_email)
