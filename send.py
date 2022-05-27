from telethon import TelegramClient
import os
import zipfile

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])
                
zip_directory('phone', 'phone.zip')
api_id = 8696891
api_hash = 'ee70f157b8efa547ca29b7d9538d234b'
client = TelegramClient('+84833655234', api_id, api_hash)

async def main():
    await client.send_file('me', 'phone.zip')

with client:
    client.loop.run_until_complete(main())