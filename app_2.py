import telebot
import requests

# Вставьте ваш токен для Telegram-бота
API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши название города, чтобы узнать погоду.")

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text.strip().lower()
    
    # Отправка запроса к API
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    try:
        weather_data = requests.get(url).json()
        
        # Получаем данные о температуре и ощущаемой температуре
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        
        # Формируем ответ
        response = (f'Погода в {city.title()}:\n'
                    f'Температура: {temperature}°C\n'
                    f'Ощущается как: {temperature_feels}°C')
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, "Не удалось получить погоду. Проверьте название города.")

# Запуск бота
bot.polling()
