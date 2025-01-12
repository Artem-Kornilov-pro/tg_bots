import telebot
import random

# Токен вашего Telegram-бота
BOT_TOKEN = ''

bot = telebot.TeleBot(BOT_TOKEN)

# Список случайных ответов
RESPONSES = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется, да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока не ясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно"
]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я - Бот Шар Судьбы. Задай мне вопрос, и я дам ответ.")

@bot.message_handler(func=lambda message: True)
def magic_ball(message):
    response = random.choice(RESPONSES)
    print(message.text, response, message.chat.first_name)
    bot.reply_to(message, response)

if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()
