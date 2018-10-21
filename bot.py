import logging
from handlers import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Bot запущен')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("frame", send_camera_frame, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo, pass_user_data=True))
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
