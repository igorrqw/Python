def hello_function(phonebook):
    print(f'Здравствуйте, текущий справочник содержит следующие данные \n {phonebook} \n' )

def get_type_export():
    num = int(input(f"Для экспорта данных в txt введите 3, для экспорта в csv введите 4 \n"))
    return num

def get_type_import():
    num = int(input(f"Данные для обновления справочника находятся в двух форматах txt и csv.\nДля импорта из txt введите 1, для импорта из csv введите 2: \n"))
    return num