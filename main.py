from sheet_reader import get_tasks_from_sheet
from drive_utils import upload_asset_to_drive
from notify import send_slack_notification, send_email
from db_logger import log_task
from report_generator import generate_daily_report
from asset_generator import generate_asset

# Read tasks from sheet
tasks = get_tasks_from_sheet()

# Process each task
for task in tasks:
    try:
        filename, asset = generate_asset(task)
        file_id = upload_asset_to_drive(filename, asset)

        # Log & Notify
        log_task(task['id'], "SUCCESS")
        send_slack_notification(f"✅ Task `{task['id']}` completed.")
    except Exception as e:
        log_task(task['id'], "FAILURE", str(e))
        send_slack_notification(f"❌ Task `{task['id']}` failed: {str(e)}")
        send_email("Task Failed", str(e))

# Generate daily report
generate_daily_report()