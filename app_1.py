#калькулятор
import telebot

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Напиши мне математическое выражение, и я вычислю его результат.")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"Результат: {result}")
    except:
        bot.reply_to(message, "Не удалось вычислить. Убедитесь, что выражение корректно.")

bot.polling()
