import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

credentials = service_account.Credentials.from_service_account_file('credentials.json')
service = build('drive', 'v3', credentials=credentials)
print(f"Service Account Email:'{credentials.service_account_email}'")

about = service.about().get(fields="user, storageQuota").execute()
print("Authenticated as:", about['user']['emailAddress'])
print("Total Storage:", about['storageQuota']['limit'])
print("Used Storage:", about['storageQuota']['usage'])

results = service.files().list(
    pageSize=10,
    fields="nextPageToken, files(id, name)",
    supportsAllDrives=True,
    includeItemsFromAllDrives=True
).execute()


files = results.get('files', [])
for f in files:
    print(f"Found file: '{f['name']}' ({f['id']})")

files = {f['name']:f['id'] for f in files}

## https://drive.google.com/drive/my-drive
file_name = "temp_video.mp4" 
file_id = files.get(file_name)
print(f"file_name:'{file_name}' file_id:'{file_id}'") 

fh = io.BytesIO()
request = service.files().get_media(fileId=file_id)
downloader = MediaIoBaseDownload(fh, request)

done = False
while done is False:
    status, done = downloader.next_chunk()
    print(f"Download {int(status.progress() * 100)}%.")

with open(file_name, 'wb') as f:
    f.write(fh.getbuffer())

print(f"File downloaded as: {file_name}")
