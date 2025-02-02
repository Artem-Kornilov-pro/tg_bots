package main

import (
	"fmt"
	"log"
	"net/http"
	//"os"
	"strings"
	"time"
	"unicode"
	"github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

// Функция для получения текущего времени
func getTime() string {
	return time.Now().Format("2006-01-02 15:04:05")
}

// Функция для получения погоды через wttr.in (без API-ключей)
func getWeather(location string) string {
	url := fmt.Sprintf("https://wttr.in/%s?format=%%C+%%t&lang=ru", location)
	resp, err := http.Get(url)
	if err != nil {
		return "Ошибка: не удалось получить данные о погоде."
	}
	defer resp.Body.Close()

	var weather string
	_, err = fmt.Fscan(resp.Body, &weather)
	if err != nil {
		return "Ошибка при чтении ответа."
	}
	return fmt.Sprintf("Погода в %s: %s", location, weather)
}

// Функция-заглушка для обработки запросов к нейросети
func processNeuralRequest(text string) string {
	return fmt.Sprintf("Нейросеть обработала запрос: %s", text)
}

func main() {
	// Читаем токен бота из переменной окружения
	token := "token"
	if token == "" {
		log.Fatal("TELEGRAM_BOT_TOKEN не установлен")
	}

	bot, err := tgbotapi.NewBotAPI(token)
	if err != nil {
		log.Fatal(err)
	}

	bot.Debug = true
	log.Printf("Авторизован как %s", bot.Self.UserName)

	updateConfig := tgbotapi.NewUpdate(0)
	updateConfig.Timeout = 60
	updates := bot.GetUpdatesChan(updateConfig)

	for update := range updates {
		if update.Message == nil {
			continue
		}

		switch update.Message.Text {
		case "/start":
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Привет! Я помощник-бот. Отправь /help, чтобы узнать мои команды.")
			bot.Send(msg)
		case "/help":
			helpText := "Я умею:\n"
			helpText += "/start - Запуск бота\n"
			helpText += "/help - Список команд\n"
			helpText += "/time - Узнать текущее время\n"
			helpText += "Введите город, чтобы узнать погоду (пример: Москва)\n"
			helpText += "Введите любой текст для обработки нейросетью"
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, helpText)
			bot.Send(msg)
		case "/time":
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, fmt.Sprintf("Текущее время: %s", getTime()))
			bot.Send(msg)
		default:
			text := strings.TrimSpace(update.Message.Text)
			if strings.IndexFunc(text, func(r rune) bool { return !(unicode.IsLetter(r) || unicode.IsSpace(r)) }) == -1 {

				msg := tgbotapi.NewMessage(update.Message.Chat.ID, getWeather(text))
				bot.Send(msg)
			} else {
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, processNeuralRequest(text))
				bot.Send(msg)
			}
		}
	}
}
