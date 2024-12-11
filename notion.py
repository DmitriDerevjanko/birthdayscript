#notion.py

import requests
import logging
import datetime
from config import NOTION_API_TOKEN, NOTION_DATABASE_ID

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_birthdays():
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Notion-Version": "2021-08-16"
    }
    logging.debug(f"Sending request to Notion API: {url}")
    
    has_more = True
    next_cursor = None
    birthdays = []

    while has_more:
        payload = {}
        if next_cursor:
            payload["start_cursor"] = next_cursor
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return []
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            return []
        
        logging.debug(f"Response status code: {response.status_code}")
        logging.debug(f"Response content: {response.content}")

        try:
            data = response.json()
        except ValueError as json_err:
            logging.error(f"JSON decode error: {json_err}")
            return []
        
        logging.debug("Data received from Notion: %s", data)

        try:
            for result in data.get('results', []):
                properties = result['properties']
                name = properties['Name']['title'][0]['text']['content']
                date_str = properties['Date']['date']['start']
                email = properties['Email']['email']
                birthday = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                birthdays.append({"name": name, "birthday": birthday, "email": email})
        except KeyError as key_err:
            logging.error(f"Key error: {key_err}")
        except IndexError as index_err:
            logging.error(f"Index error: {index_err}")
        except Exception as err:
            logging.error(f"An error occurred while processing data: {err}")

        has_more = data.get("has_more", False)
        next_cursor = data.get("next_cursor", None)
    
    logging.debug(f"Birthdays extracted: {birthdays}")
    return birthdays

if __name__ == "__main__":
    birthdays = get_birthdays()
    logging.info(f"Retrieved birthdays: {birthdays}")
