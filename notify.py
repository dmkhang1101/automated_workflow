import requests
import os
from config import SLACK_WEBHOOK_URL, SENDER_EMAIL, RECEIVER_EMAIL, EMAIL_PASSWORD
import yagmail

def send_slack_notification(message):
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, json=payload)

def send_email(subject, body):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, EMAIL_PASSWORD)
        yag.send(to=RECEIVER_EMAIL, subject=subject, contents=body)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_email_with_attachment(subject, body, attachment_path):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, EMAIL_PASSWORD)
        yag.send(
            to=RECEIVER_EMAIL,
            subject=subject,
            contents=[body, attachment_path]
        )
        print("Email with report sent successfully.")
    except Exception as e:
        print(f"Error sending email with report: {e}")