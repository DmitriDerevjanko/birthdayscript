# test_email_sender.py

from email_sender import send_email

test_recipients = ['dmitri.derevjanko@taltech.ee']

send_email("Test Subject", "This is a test email body.", test_recipients)

print("Test email sent!")
