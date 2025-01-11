import telebot

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
tasks = []

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет! Напиши /add задача, чтобы добавить задачу, /list, чтобы увидеть список, или /delete номер, чтобы удалить задачу.")

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
        bot.reply_to(message, "Список задач:\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)))
    else:
        bot.reply_to(message, "Список задач пуст.")

@bot.message_handler(commands=['delete'])
def delete_task(message):
    try:
        task_number = int(message.text[8:])  # Получаем номер задачи после команды
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)  # Удаляем задачу по номеру
            bot.reply_to(message, f"Задача '{deleted_task}' удалена!")
        else:
            bot.reply_to(message, "Неверный номер задачи.")
    except ValueError:
        bot.reply_to(message, "Укажите номер задачи после команды /delete.")
    except IndexError:
        bot.reply_to(message, "Задача с таким номером не существует.")

bot.polling()
