# ⚙️ AI Asset Automation Workflow

## 📌 Overview  
An automated pipeline that retrieves task descriptions from Google Sheets, generates AI-powered assets using OpenAI, uploads them to Google Drive, and sends real-time notifications via Slack and Email.

---

## 🚀 Features

- 📄 Read tasks from Google Sheets  
- 🎨 Generate images (PNG, JPG), audio (MP3), and text assets using OpenAI  
- ☁️ Upload assets directly to Google Drive  
- 🔔 Get notified via Slack and Email upon task completion or failure  
- 📊 Daily report generation for processed tasks  
- 🔁 Optional scheduled automation (run at specific intervals)  

---

## 🛠️ Setup Instructions

### 1. Install dependencies  
```bash
pip install -r requirements.txt
```

### 2. Google Service Account
Create a service_account.json file with your Google Service Account credentials.
Make sure this account has access to both the target Google Sheet and the destination Google Drive folder.

### 3. Configure Environment Variables
Copy the example .env file and fill in your configuration values:
```bash
cp .env.example .env
```
Edit .env to include:

OpenAI API key
Google Sheet ID
Google Drive Folder ID
Slack Webhook URL
Email SMTP credentials

### 4. Run the Workflow
Run once manually:
```bash
python3 main.py
```

Run automatically on a schedule:
```bash
python3 scheduler.py
```

## 📁 Project Structure
```bash
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
```