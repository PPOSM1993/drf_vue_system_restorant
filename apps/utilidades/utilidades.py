#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

import environ

env = environ.Env()
environ.Env.read_env()

load_dotenv()



def sendMail(html, asunto, para):
    msg = MIMEMultipart('alternave')
    msg['Subject'] = asunto
    msg['From'] =  os.getenv("SMTP_USER")
    msg['To'] = para
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        server.sendmail(os.getenv("SMTP_USER"), para, msg.as_string())
        server.quit()
    except smtplib.SMTPResponseException as e:
        print("error envío mail")