import telebot

BOT_TOKEN = "7234251185:AAHHnUp9H1PpxYc4g8DEwKzCmCuma7YtB_Q"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_members(message):
    for new_member in message.new_chat_members:
        first_name = new_member.first_name
        welcome_message = f'Добро пожаловать, {first_name}! Пожалуйста представь себя в разделе #Осебе'
        bot.send_message(message.chat.id, welcome_message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
