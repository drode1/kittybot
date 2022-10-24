import logging

import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

from settings import BOT_TOKEN, LOGGING_FORMAT

URLS = {
    'cat': 'https://api.thecatapi.com/v1/images/search',
    'dog': 'https://api.thedogapi.com/v1/images/search',
}


def get_new_image(value):
    try:
        response = requests.get(URLS.get(value))
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_animal = response[0].get('url')
    return random_animal


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image('cat'))


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image('dog'))


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup(
        [['/newcat'], ['/newdog']], resize_keyboard=True,
    )

    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри какого котика я тебе нашел',
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_new_image('cat'))


def main():
    updater = Updater(token=BOT_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logging.basicConfig(
        filename='program.log',
        level=logging.DEBUG,
        format=LOGGING_FORMAT,
    )
    main()
