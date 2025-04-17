from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import mimetypes
from config import GOOGLE_SERVICE_ACCOUNT, DRIVE_FOLDER_ID

creds = service_account.Credentials.from_service_account_file(
    GOOGLE_SERVICE_ACCOUNT,
    scopes=['https://www.googleapis.com/auth/drive']
)
drive_service = build('drive', 'v3', credentials=creds)

def upload_asset_to_drive(filename, content):
    # Determine the MIME type
    ext = os.path.splitext(filename)[1].lower()
    mime_type, _ = mimetypes.guess_type(filename)

    # Define temp path
    temp_path = f"/tmp/{filename}"

    # Save the content to a file depending on type
    if isinstance(content, str):
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(content)
    elif isinstance(content, bytes):
        with open(temp_path, "wb") as f:
            f.write(content)
    else:
        raise ValueError("Unsupported content type. Must be str or bytes.")

    # Upload to Drive
    file_metadata = {'name': filename, 'parents': [DRIVE_FOLDER_ID]}
    media = MediaFileUpload(temp_path, mimetype=mime_type or 'application/octet-stream')

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    return file.get('id')
