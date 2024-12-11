import logging
from slack_sender import send_slack_message

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

test_message = "This is a test message sent to Slack!"

logging.debug("Sending test Slack message")
response = send_slack_message(test_message)

logging.debug("Slack response received")
print("Slack response:", response)
