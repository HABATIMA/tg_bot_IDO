import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters



import requests


telegram_token = "6325381745:AAH-QqE7pGYgzk8lhEJUHnJNmkrzxduke2o"


openai_api_key = "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"


gpt_endpoint = "https://api.openai.com"


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я готов отвечать на ваши запросы.")


def handle_text(update, context):
    input_text = update.message.text

    
    gpt_response = send_request_to_gpt(input_text)

    
    context.bot.send_message(chat_id=update.effective_chat.id, text=gpt_response)


def send_request_to_gpt(input_text):
    url = gpt_endpoint + "?text=" + input_text

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai_api_key
    }

    response = requests.get(url, headers=headers)
    gpt_response = response.text

    return gpt_response

def main():
    # Инициализация бота
    updater = Updater(token=telegram_token)
    dp = updater.dispatcher

    # Установка обработчиков команд и текстовых сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.Text & ~filters.command, handle_text))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
