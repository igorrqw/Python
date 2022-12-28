def start(update, context):
    update.message.reply_text(
        "Привет. Это телефонный справочник\n"
        "Чтобы узнать список доступных операций, введите команду /help")


def help(update, context):
    update.message.reply_text(
        'Выберете команду: \n 1 - показать всех сотрудников \n 2 - добавить сотрудника \n 3 - найти сотрудника по фамилии \n 4 - удалить сотрудника \n show - показать список команд \n stop - остановить \n'
        'Пример команды "2" для добавления сотрудника: "/2 Иванов"')