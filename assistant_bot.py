import telebot

TOKEN = 'your code'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать в поддержку пользователей!")


@bot.message_handler(commands=['services'])
def send_info(message):
    bot.send_message(message.chat.id,
    "Услуги по печати на футболках:\n"
    "Стандартная печать\n"
    "Цифровая печать\n"
    "Термотрансферная печать\n"
    "Прямая печать на ткани (DTG)\n"
    "Вышивка")

@bot.message_handler(commands=['sizes'])
def handle_sizes(message):
    bot.send_message(message.chat.id,
    "Размерная сетка:\n"
    "XS: 88 см (обхват груди), 68 см (длина)\n"
    "S: 94 см (обхват груди), 70 см (длина)\n"
    "M: 100 см (обхват груди), 72 см (длина)\n"
    "L: 106 см (обхват груди), 74 см (длина)\n"
    "XL: 112 см (обхват груди), 76 см (длина)\n"
    "XXL: 118 см (обхват груди), 78 см (длина)")

@bot.message_handler(commands=['complaint'])
def handle_complaint(message):
    complaint_text = message.text

    with open("complaint.txt", "a", encoding="utf-8") as file:
        file.write(complaint_text + "\n")

    bot.send_message(message.chat.id, "Ваша жалоба сохранена")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    questions ="как сделать заказ?", "можно делать свой дизайн?", "сколько занимает времени?"
    if message.text.lower() == "/question":
        bot.send_message(message.chat.id, f"часто задаваемые вопросы: {questions}")
    elif message.text.lower() == "как сделать заказ?":
        bot.send_message(message.chat.id, "в приложении")
    elif message.text.lower() == "можно делать свой дизайн?":
        bot.send_message(message.chat.id, "да")
    elif message.text.lower() == "сколько занимает времени?":
        bot.send_message(message.chat.id, "3 - 5 дней")


bot.polling(none_stop=True)
