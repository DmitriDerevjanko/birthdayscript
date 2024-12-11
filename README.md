# Birthday and Reminder Automation System

This project automates birthday greetings and reminders using Notion, Slack, and email notifications. It features scheduled tasks to send birthday wishes and reminders to specified contacts.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [License](#license)

---

## Features

- **Birthday Automation**: Automatically sends birthday greetings via email and Slack.
- **Reminder Notifications**: Sends reminders for upcoming birthdays.
- **Integration**:
  - Notion API for retrieving birthday data.
  - Gmail SMTP for sending email notifications.
  - Slack API for team notifications.
- **Customizable Templates**: Use styled HTML emails for greetings.
- **Scheduler**: Daily execution of tasks at a defined time.

---

## Technologies Used

- **Languages**: Python
- **APIs**:
  - Notion API
  - Slack API
  - SMTP for email
- **Libraries**:
  - `smtplib`
  - `email.mime`
  - `requests`
  - `schedule`
  - `pytz`

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DmitriDerevjanko/birthdayscript.git
   cd birthdayscript
   ```

2. Create a `.env` file in the root directory and configure the environment variables (see [Configuration](#configuration)).

---

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
NOTION_API_TOKEN=your_notion_api_token
NOTION_DATABASE_ID=your_notion_database_id

SMTP_SERVER=smtp.zone.eu
SMTP_PORT=587
EMAIL_ADDRESS=email@example.com
EMAIL_PASSWORD=your_email_password

SLACK_TOKEN=your_slack_token
SLACK_CHANNEL=#üldine

REMINDER_EMAILS=email1@example.com,email2@example.com
```

### `config.py`

The application loads sensitive information from the `.env` file using the `os` module. Ensure the `.env` file is correctly set up before running the application.

---

## Usage

1. Start the scheduler:

   ```bash
   python main.py
   ```

2. The scheduler runs tasks daily at 08:00 AM Tallinn time. Adjust the schedule in `scheduler.py` if needed.

3. Test email notifications:

   ```bash
   python test_email_sender.py
   ```

4. Test Slack notifications:

   ```bash
   python test_slack_sender.py
   ```

---

## Project Structure

```plaintext
birthday-reminder-system/
├── config.py         # Environment variable loader
├── email_sender.py   # Email notification logic
├── notion.py         # Fetches birthday data from Notion
├── scheduler.py      # Scheduler for running tasks
├── slack_sender.py   # Slack notification logic
├── test_email_sender.py # Email sender testing script
├── test_slack_sender.py # Slack sender testing script
├── .env              # Environment variables (not included in version control)
└── README.md         # Project documentation
```

