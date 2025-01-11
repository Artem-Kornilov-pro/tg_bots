#анекдоты
import telebot
import random

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)

jokes = [
    "Почему программисты не голодают? Потому что у них всегда есть бутстрап!",
    "Как программисты здороваются? Ctrl+C и Ctrl+V.",
    "Почему Python любит детей? Потому что у него есть глобальные переменные.",
]

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Напиши /joke, чтобы услышать шутку.")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, random.choice(jokes))

bot.polling()
