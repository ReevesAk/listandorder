import smtplib
from email.mime.text import MIMEText
import smtplib
import time
import math
import random

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender, password)
      smtp_server.sendmail(sender, recipients, msg.as_string())
    

def verify_otp(otp_receieved: str, otp_sent: str):
    if otp_receieved == otp_sent:
        return True
    else:
        return False


def generate_otp():
   digits="0123456789"
   OTP=""
   for i in range(6):
      OTP+=digits[math.floor(random.random()*10)]
   return OTP
