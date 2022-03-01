import telebot
bot = telebot.TeleBot("5173440304:AAGOO6PhsDxOdKwCfpeOgHwPquwRd90jc3w")
@bot.message_handler(commands=["start"])
def start(message, res = False):
    chat_id = message.chat.id
    bot.send_message(chat.id, text)
