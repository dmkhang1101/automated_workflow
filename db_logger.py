import sqlite3
from datetime import datetime
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS task_logs (
            task_id TEXT,
            status TEXT,
            error_msg TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def log_task(task_id, status, error_msg=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO task_logs (task_id, status, error_msg, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (task_id, status, error_msg, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
