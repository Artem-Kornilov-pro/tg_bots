import telebot
import requests

API_TOKEN = "YOUR_BOT_API_TOKEN"
YANDEX_API_KEY = "YOUR_YANDEX_API_KEY"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Напиши текст на любом языке, и я переведу его на английский.")

@bot.message_handler(func=lambda message: True)
def translate(message):
    text = message.text
    url = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={YANDEX_API_KEY}&text={text}&lang=en"
    try:
        response = requests.get(url)
        data = response.json()
        translation = data.get("text", ["Ошибка перевода"])[0]
        bot.reply_to(message, f"Перевод: {translation}")
    except:
        bot.reply_to(message, "Ошибка при переводе текста.")

bot.polling()
