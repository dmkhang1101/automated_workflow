import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from config import DB_FILE
from notify import send_email_with_attachment

def generate_daily_report():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    today = datetime.utcnow().date()
    start = datetime.combine(today, datetime.min.time()).isoformat()
    end = datetime.combine(today + timedelta(days=1), datetime.min.time()).isoformat()

    cursor.execute(
        "SELECT status, COUNT(*) FROM task_logs WHERE timestamp BETWEEN ? AND ? GROUP BY status",
        (start, end)
    )
    data = dict(cursor.fetchall())
    conn.close()

    # Plot
    labels = list(data.keys())
    values = list(data.values())
    colors = ['green' if label == 'SUCCESS' else 'red' for label in labels]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=colors)
    plt.title("Daily Task Summary")
    plt.xlabel("Status")
    plt.ylabel("Number of Tasks")
    plt.tight_layout()
    report_filename = "daily_report.png"
    plt.savefig(report_filename)
    plt.close()

    # Email summary
    summary = "\n".join([f"{status}: {count}" for status, count in data.items()])
    subject = "📊 Daily Automation Report"
    body = f"Here is the task summary for {today}:\n\n{summary}"

    send_email_with_attachment(subject, body, report_filename)

