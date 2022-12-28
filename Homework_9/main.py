# Прикрутить бота к задаче о телефонном справочнике. Бот должен показать весь телефонный справочник, найти по фамилии,
# а также предоставить возможность добавлять и удалять записи в справочнике. 
# Проект выложить на гитхаб, добавить файл requirements.txt, в котором указать необходимые библитеки для установки. 
# Папку venv загружать на гитхаб не нужно!


import logging
from view import*
from models import*

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5606378948:AAHnfgQsWHlCg82o9h6rLVse9nZLyB3vHLE'


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('1', show_employees))
    dp.add_handler(CommandHandler('2', add_employess_to_list))
    dp.add_handler(CommandHandler('3', find_employess))
    dp.add_handler(CommandHandler('4', del_employess))
    dp.add_handler(CommandHandler('stop', stop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
