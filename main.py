import telebot
from telebot import types

bot = telebot.TeleBot("5144376489:AAEsR4EM0rswAp5EjcxsRhe9UWN59KW0Poo")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     "Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты",
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Факт":
        answer = "забавный факт"
    elif message.text.strip() == "Поговорка":
        answer = "русская поговорка"
    bot.send_message(message.chat.id, answer)


print("start")
bot.polling(none_stop=True, interval=0)

