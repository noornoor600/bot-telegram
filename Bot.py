import telebot

tk = "seu token"

rob = telebot.TeleBot(tk)

@rob.message_handler(commands=["start", "ola", "oi"])

def primeira_msg(message):

    id = message.chat.id

    rob.send_message(id, "Olá amigo")

rob.polling()
