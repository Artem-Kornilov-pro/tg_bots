import telebot
import requests
import os
from datetime import datetime

# Инициализация бота
TOKEN = "your token"
bot = telebot.TeleBot(TOKEN)

# Функция для получения текущего времени
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Функция для получения погоды через wttr.in (без API-ключей)
def get_weather(location):
    url = f"https://wttr.in/{location}?format=%C+%t&lang=ru"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Ошибка: не удалось получить данные о погоде."
        
        return f"Погода в {location}: {response.text}"
    except Exception as e:
        return f"Ошибка получения погоды: {str(e)}"


# Функция для обработки запросов к нейросети (заглушка)
def process_neural_request(text):
    return f"Нейросеть обработала запрос: {text}"

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я помощник-бот. Отправь /help, чтобы узнать мои команды.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Я умею:\n"
    help_text += "/start - Запуск бота\n"
    help_text += "/help - Список команд\n"
    help_text += "/time - Узнать текущее время\n"
    help_text += "Введите город, чтобы узнать погоду (пример: Москва)\n"
    help_text += "Введите любой текст для обработки нейросетью"
    bot.reply_to(message, help_text)

# Обработчик команды /time
@bot.message_handler(commands=['time'])
def send_time(message):
    bot.reply_to(message, f"Текущее время: {get_time()}")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.strip()
    if text.replace(" ", "").isalpha():  # Проверяем, что введен город (слово без цифр)
        bot.reply_to(message, get_weather(text))
    else:
        bot.reply_to(message, process_neural_request(text))

if __name__ == "__main__":
    bot.polling(none_stop=True)
