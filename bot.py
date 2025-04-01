import telebot

BOT_TOKEN = ""
ADMIN_CHAT_ID = ''

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

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Добро пожаловать в Blue Chips — пространство для людей, ценящих качественные связи и взаимопомощь! "
        "Вместе мы создаем сеть полезных контактов и открываем новые возможности для роста.\n"
        "<b>Расскажите немного о себе в одном сообщении, чтобы мы могли узнать про вас.</b>"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="HTML")
    # bot.send_message(message.chat.id, f"Ваш chat_id: {message.chat.id}") получить ADMIN_CHAT_ID 

# Функция, обрабатывающая любые входящие сообщения кандидата
@bot.message_handler(func=lambda message: True)
def handle_introduction(message):
    # Пересылаем сообщение кандидата администратору
    bot.forward_message(ADMIN_CHAT_ID, message.chat.id, message.message_id)
    
    # Формируем дополнительное сообщение с данными кандидата
    username = message.from_user.username if message.from_user.username else "не указан"
    info_text = f"Username кандидата: @{username}" if username != "не указан" else "Username кандидата не указан."
    bot.send_message(ADMIN_CHAT_ID, info_text)
    
    # Отправляем ответ кандидату
    response_text = "Спасибо за информацию! Мы рассмотрим твоё сообщение и скоро дадим обратную связь."
    bot.send_message(message.chat.id, response_text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
