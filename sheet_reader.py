from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_SERVICE_ACCOUNT,SPREADSHEET_ID,RANGE_NAME

def get_tasks_from_sheet():
    creds = service_account.Credentials.from_service_account_file(
        GOOGLE_SERVICE_ACCOUNT,
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
    )
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    tasks = []
    for row in values:
        tasks.append({
            'id': row[0],
            'description': row[1],
            'asset_url': row[2],
            'output_format': row[3],
            'model': row[4]
        })
    return tasks
