from telegram.client import Telegram

# Token do usuário 
TOKEN_USER = '1016353473_6802340938325777775'
# Token do chat do grupo remetente
CHAT_ID_SENDER = '-453876445'
# Token do chat do grupo destinatário
CHAT_ID_RECEIVER = '366089799'


# API info
api_id = 1872826
api_hash = '644c4661860ead457b0dbaff76203f07'
phone_number = '+556984224860'
dbenc = 'chappie'


client = Telegram(
    api_id=api_id,
    api_hash=api_hash,
    phone=phone_number,
    database_encryption_key=dbenc,
)

client.login(blocking=False)
