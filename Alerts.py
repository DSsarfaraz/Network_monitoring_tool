"""
Alerts Module
=============
This module sends email alerts when a device is unreachable.
"""

import smtplib
from email.mime.text import MIMEText

def send_alert(email, subject, message):
    """
    Send an email alert.

    Args:
        email (str): The recipient's email address.
        subject (str): The subject of the email.
        message (str): The body of the email.
    """
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")