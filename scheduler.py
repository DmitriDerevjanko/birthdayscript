import schedule
import time
import datetime
import logging
import pytz
from notion import get_birthdays
from email_sender import send_email
from slack_sender import send_slack_message
from config import REMINDER_EMAILS

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

tallinn_timezone = pytz.timezone('Europe/Tallinn')

def check_birthdays():
    today = datetime.datetime.now(tallinn_timezone).date()
    birthdays = get_birthdays()
    
    for entry in birthdays:
        name = entry['name']
        birthday = entry['birthday']
        email = entry['email']
        
        if birthday.month == today.month and birthday.day == today.day:
            subject = f"Palju õnne sünnipäevaks, {name}!"
            body = f"Tere {name}, soovime Sulle palju õnne ja tervist sinu sünnipäevaks!"
            send_email(subject, body, [email])
            send_slack_message(body, is_birthday=True)
        elif birthday.month == today.month and (birthday.day - today.day) == 5:
            subject = f"Meeldetuletus: {name} sünnipäev 5 päeva pärast"
            body = f"Tere, tuletame meelde, et {name} sünnipäev on 5 päeva pärast."
            send_email(subject, body, REMINDER_EMAILS)

schedule.every().day.at("08:00").do(check_birthdays)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)  

if __name__ == "__main__":
    logging.info("Starting scheduler...")
    run_scheduler()
