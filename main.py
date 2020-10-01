from telegram.client import Telegram
from json import dumps
from secret import *


client = Telegram(
    api_id=API_ID,
    api_hash=API_HASH,
    phone=PHONE_NUMBER,
    database_encryption_key=DBENC,
)


client.login()


def new_message_handler(update):  
    print(dumps(update['message']['chat_id'], indent=4))
    if str(update['message']['chat_id']) == CHAT_ID_SENDER:
        print(dumps(update, indent=4))
        message_content = update['message']['content'].get('text', {})
        message_entities = message_content.get('entities', '')
        message_text = message_content.get('text', {})
        print('\n\n\n', 'Encaminhando mensagem', '\n\n\n')
        client.send_message(
            chat_id=CHAT_ID_RECEIVER,
            text=message_text,
        )


client.add_message_handler(new_message_handler)
client.idle()
