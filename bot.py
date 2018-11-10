import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import check_photo, send_frame, talk_to_me, greet_user
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log',
                    )


def main():
    mybot = Updater(settings.TELEGRAM_API, request_kwargs=settings.PROXY)
    logging.info('Bot запущен')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('frame', send_frame, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.photo, check_photo, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
