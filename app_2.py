import telebot

# Замените на токен вашего Telegram-бота
API_TOKEN = ""

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    """
    Приветственное сообщение для пользователя.
    """
    bot.reply_to(message, "Привет! Напиши название города, чтобы получить ссылку на прогноз погоды.")

@bot.message_handler(func=lambda message: True)
def send_weather_link(message):
    """
    Генерация ссылки на прогноз погоды для указанного города.
    """
    city = message.text.strip()
    city_encoded = city.replace(" ", "+")
    weather_url = f"https://www.google.com/search?q=погода+{city_encoded}"
    bot.reply_to(
        message,
        f"Вот ссылка на прогноз погоды для города *{city}*:\n[Погода в {city}]({weather_url})",
        parse_mode='Markdown'
    )

# Запуск бота
bot.polling()
