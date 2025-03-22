import telebot

BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_members(message):
    for new_member in message.new_chat_members:
        first_name = new_member.first_name
        welcome_message = (
            f"Добро пожаловать, {first_name}! "
            "Пожалуйста представь себя в разделе "
            "<a href='https://t.me/c/2559274539/56'>О себе</a>."
        )
        bot.send_message(message.chat.id, welcome_message, parse_mode="HTML")

if __name__ == '__main__':
    bot.polling(none_stop=True)
