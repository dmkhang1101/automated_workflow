# AI Asset Automation Workflow

## Overview
An automated pipeline that retrieves task descriptions from Google Sheets, generates AI-powered assets using OpenAI, uploads them to Google Drive, and sends real-time notifications via Slack and Email.

## Features

📄 Read tasks from Google Sheets
🎨 Generate images (PNG, JPG), audio (MP3), and text assets using OpenAI
☁️ Upload assets directly to Google Drive
🔔 Get notified via Slack and Email upon task completion or failure
📊 Daily report generation for processed tasks
🔁 Optional scheduled automation (run at specific intervals)

## Setup Instructions

1. Install dependencies
pip install -r requirements.txt

2. Google Service Account
Create a service_account.json file with your Google Service Account credentials. Make sure it has access to your target Google Sheet and Drive folder.

3. Configure Environment Variables
Copy the example file and fill in the necessary values:

cp .env.example .env
Edit .env with your actual API keys and config values

4. Run the Workflow
To run once manually:
python main.py

To run automatically on a schedule:
python scheduler.py
⏰ Automation Options

You can automate the workflow via:

scheduler.py (Python-based scheduling using schedule module)
cron job (for server-based scheduling)
GitHub Actions (for cloud-based scheduled runs)
Zapier/n8n (for low-code automation with integrations)

## Project Structure

.
├── main.py               # Core pipeline
├── scheduler.py          # For scheduled automation
├── asset_generator.py    # OpenAI integration logic
├── drive_utils.py        # Google Drive upload
├── sheet_reader.py       # Read tasks from Google Sheets
├── notify.py             # Slack and Email notifications
├── db_logger.py          # Task logging
├── report_generator.py   # Daily task summary report
├── .env.example          # Environment variable template
├── service_account.json  # Google Service Account credentials


## Powered By

OpenAI API
Google Sheets API
Google Drive API
Slack Webhooks
SMTP Email
