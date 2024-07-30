import os
import urllib.request
import urllib.parse

def send_sms(recipient: str, message: str):
    try:
        data = urllib.parse.urlencode({
            'apikey': os.getenv("TEXTLOCAL_API_KEY"),
            'numbers': recipient,
            'message': message,
            'sender': os.getenv("TEXTLOCAL_SENDER")
        })
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        print(fr)
    except Exception as e:
        print(f"Failed to send SMS: {e}")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to: str, subject: str, body: str):
    try:
        gmail_user = os.getenv("GMAIL_USERNAME")
        gmail_password = os.getenv("GMAIL_PASSWORD")

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, to, text)
        server.quit()
        
        print(f"Email sent to: {to}")
    except Exception as e:
        print(f"Failed to send email: {e}")
