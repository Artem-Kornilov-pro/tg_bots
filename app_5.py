#список задача
import telebot

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
tasks = []

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Напиши /add задача, чтобы добавить задачу, или /list, чтобы увидеть список.")

@bot.message_handler(commands=['add'])
def add_task(message):
    task = message.text[5:]
    if task:
        tasks.append(task)
        bot.reply_to(message, f"Задача '{task}' добавлена!")
    else:
        bot.reply_to(message, "Напишите задачу после команды /add.")

@bot.message_handler(commands=['list'])
def list_tasks(message):
    if tasks:
        bot.reply_to(message, "Список задач:\n" + "\n".join(f"- {t}" for t in tasks))
    else:
        bot.reply_to(message, "Список задач пуст.")

bot.polling()
