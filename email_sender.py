# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from config import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject, body, to_emails):
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(to_emails)

    # HTML part
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
            }}
            .container {{
                width: 100%;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }}
            .header {{
                background-color: #000000;
                color: white;
                padding: 10px 0;
                text-align: center;
                border-radius: 10px 10px 0 0;
            }}
            .content {{
                padding: 20px;
                text-align: center;
                color: #000000;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                color: #000000;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>{subject}</h1>
            </div>
            <div class="content">
                <p>{body}</p>
            </div>
            <div class="footer">
                <p>Parimate soovidega,<br>AIRE tiim</p>
            </div>
        </div>
    </body>
    </html>
    """

    part = MIMEText(html, "html")
    msg.attach(part)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_emails, msg.as_string())
        logging.info(f"Email sent to {to_emails}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")
