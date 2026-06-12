import smtplib

from email.mime.text import (
    MIMEText
)

def send_alert(
    receiver,
    message
):

    sender = "yourmail@gmail.com"

    password = "app_password"

    msg = MIMEText(message)

    msg['Subject'] = (
        "Inventory Alert"
    )

    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP(
        'smtp.gmail.com',
        587
    )

    server.starttls()

    server.login(
        sender,
        password
    )

    server.send_message(msg)

    server.quit()