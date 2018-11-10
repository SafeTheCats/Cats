import logging
import os
import time

import clarifai
from clarifai.rest import ClarifaiApp

import settings


def is_cat(file_name):
    image_has_cat = False
    try:
        app = ClarifaiApp(api_key=settings.CLARIFAI_API)
        model = app.public_models.general_model
        response = model.predict_by_filename(file_name, max_concepts=200)
        if response['status']['code'] == 10000:
            for concept in response['outputs'][0]['data']['concepts']:
                if concept['name'] == 'cat':
                    logging.info(concept['value'])
                    image_has_cat = True
    except clarifai.errors.ApiError:
        logging.info('clarifai.errors.ApiError')
    return image_has_cat


def greet_user(bot, update, user_data):
    text = '''Приветствую, {}! Вы используете бота - Safer-Cats.
\nЭто бот, который определяет наличие кота на фотографии, проект разработан в рамках курса Learn Python!
\nВведите команду /frame'''.format(update.message.chat.first_name)
    logging.info('greet user')
    update.message.reply_text(text)


def talk_to_me(bot, update, user_data):
    user_text = 'Привет, {}! Ты написал {}. Введи команду /frame'.format(update.message.chat.first_name,
                                                                        update.message.text)
    logging.info('User: {}, Chat id: {}, message: {}'.format(update.message.chat.username,
                                                            update.message.chat.id, update.message.text))
    update.message.reply_text(user_text)


def send_frame(bot, update, user_data):
    while True:
        if is_cat('gray.jpg'):
            bot.send_photo(chat_id=update.message.chat.id, photo=open('gray.jpg', 'rb'))
            logging.info('Кот обнаружен')
            time.sleep(30)
        else:
            time.sleep(5)


def check_photo(bot, update, user_data):
    update.message.reply_text('Обрабатываю фото')
    os.makedirs('downloads', exist_ok=True)
    photo_file = bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', '{}.jpg'.format(photo_file.file_id))
    photo_file.download(filename)

    if is_cat(filename):
        update.message.reply_text('Обнаружен котик, добавляю в библиотеку')
        new_filename = os.path.join('images', 'cat_{}.jpg'.format(photo_file.file_id))
        os.rename(filename, new_filename)
    else:
        update.message.reply_text('Котик не обнаружен')
        os.remove(filename)
