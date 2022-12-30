from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import logging
import emoji
import random

TOKEN = "5606378948:AAHnfgQsWHlCg82o9h6rLVse9nZLyB3vHLE"


reply_keyboard = [['/play', '/setting', '/rules', '/close', 'stop']]


candies = 50
step = 20
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def start(update, context):
    global candies
    candies = 50
    name = f"{update.message.from_user.first_name}"
    update.message.reply_text(
        f"Привет, {name}!{emoji.emojize(':hand:', language='alias')} Давай поиграем?{emoji.emojize(':video_game:')}\n{emoji.emojize(':one:', language='alias')}Чтобы узнать правила игры нажми  /rules\n{emoji.emojize(':two:', language='alias')}Начать игру нажми /play"
        f"\n{emoji.emojize(':three:', language='alias')}Изменить настройки нажми /settings\n{emoji.emojize(':four:', language='alias')}Закрыть клавиатуру нажми /close\n{emoji.emojize(':five:', language='alias')}Остановить бота - введи команду "
        f"/stop или нажмите кнопку /stop",
        reply_markup=markup
    )



def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "В начале игры нужно определить количество конфет на кону и количество конфет которое можно взять за один раз")

        
def settings(update, context):
    update.message.reply_text("Введите количество конфет на кону и максимально возможное количество на ход")
    return 1


def set_settings(update, context):
    global candies
    global step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text("Правила установлены, начинаем!")
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(f"На кону {candies} {emoji.emojize(':candy:')}. Ваш ход. Какое количество {emoji.emojize(':candy:')} вы берете?"
                              f"(Максимальное = {step} ) ")
    return 1 


def play_step(update, context):
    global candies
    candiy = int(update.message.text)
    if candiy == 0: 
        update.message.reply_text(f"Нужно взять {emoji.emojize(':candy:', language='alias')}")
        return 1
    if candiy > step:
        update.message.reply_text(f"Число должно быть меньше {step}!")
        return 1
    candies -= candiy
    if candies == 0:
        update.message.reply_text(f"Поздравляю, Вы победили!{emoji.emojize(':tada:', language='alias')}", reply_markup=markup)
        candies = 50
        return ConversationHandler.END
    if candies <= step:
        update.message.reply_text(f"Игра окончена, я забираю оставшиеся {emoji.emojize(':candy:', language='alias')}, я победил! ", reply_markup=markup)
        candies = 50
        return ConversationHandler.END
    else:
        if candies % (step + 1) == 0:
            update.message.reply_text(f"На кону {candies} {emoji.emojize(':candy:', language='alias')}, я беру {random.randint(1, step)}, следующий ход ваш ")
            candies -= random.randint(1, step)
        else:
            update.message.reply_text(f"На кону {candies} {emoji.emojize(':candy:', language='alias')}, я беру {candies % (step + 1)},\nОсталось конфет {candies - candies % (step + 1)}")
            candies -= candies % (step + 1)



def stop(update,context):
    update.message.reply_text(f"Всего доброго!{emoji.emojize(':hand:', language='alias')}")
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    settings_hundler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_hundler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(settings_hundler)
    dp.add_handler(play_hundler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()