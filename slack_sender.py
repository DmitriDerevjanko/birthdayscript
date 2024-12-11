import requests
import logging
from config import SLACK_TOKEN, SLACK_CHANNEL

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_slack_message(message, is_birthday=False, is_reminder=False):
    logging.debug("Preparing Slack message payload")
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_TOKEN}'
    }
    
    # Adding emojis based on the type of message
    if is_birthday:
        message = f"🎂🎉🎈 {message} 🎂🎉🎈"
    elif is_reminder:
        message = f"⏰📅 {message} 📅⏰"

    payload = {
        'channel': SLACK_CHANNEL,
        'blocks': [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{message}*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Soovib AIRE tiim"
                }
            }
        ]
    }
    logging.debug(f"Payload: {payload}")

    try:
        response = requests.post(url, headers=headers, json=payload)
        logging.debug(f"Slack response status code: {response.status_code}")
        logging.debug(f"Slack response text: {response.text}")
        return response.json()
    except Exception as e:
        logging.error(f"Error sending Slack message: {e}")
        return {'ok': False, 'error': str(e)}
