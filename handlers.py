import logging
import os
import time

from camer_frame import get_cv2
from utils import is_cat


def greet_user(bot, update):
    text ='''Приветствую, вы используете бота - Find Cat.
\nЭто бот, который определяет наличие кота на фотографии, проект разработан в рамках курса Learn Python! '''
    update.message.reply_text(text)


def send_camera_frame(bot, update, user_data):
    while True:
        if is_cat('gray.jpg'):
            bot.send_photo(chat_id=update.message.chat.id, photo=open('gray.jpg', 'rb'))
            time.sleep(5)
            logging.info('Кот обнаружен')
        else:
            time.sleep(1)


def check_user_photo(bot, update, user_data):
    update.message.reply_text('Обрабатываю фото')
    os.makedirs('downloads', exist_ok=True)                                     # создает директорию downloads
    photo_file = bot.getFile(update.message.photo[-1].file_id)                  #
    filename = os.path.join('downloads', '{}.jpg'.format(photo_file.file_id))   # берет из директории downloads файл
    photo_file.download(filename)

    if is_cat(filename):
        update.message.reply_text('Обнаружен котик, добавляю в библиотеку')
        new_filename = os.path.join('images', 'cat_{}.jpg'.format(photo_file.file_id))
        os.rename(filename, new_filename)
    else:
        update.message.reply_text('Котик не обнаружен')
        os.remove(filename)
