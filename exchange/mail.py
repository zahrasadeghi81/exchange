import smtplib
import requests
from config import rules
from email.mime.text import MIMEText


def send_smtp_email(subject , body):
    msg=MIMEText(body)
    msg['subject']= subject
    msg['From']= ""
    msg['To'] = rules['email']['receiver']

    with smtplib.SMTP('' , 777) as mail_server:
        mail_server.login('' , '')
        mail_server.sendmail(msg['from'] , msg['To'] , msg.as_string())
        # mail_server.quit()