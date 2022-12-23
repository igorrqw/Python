import logging


def show_menu():
    print('Выберете команду: \n 1 - показать всех сотрудников \n 2 - добавить сотрудника \n 3 - изменить данные сотрудника \n 4 - удалить сотрудника \n 5 - импортировать данные \n 6 - экспортировать данные ')
    
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6]:
            raise ValueError
        return select 
    except Exception:
        logging.error(f"Введена неверная команда: {select}")
        exit()


def show_employees(spisok):
    print('Список всех сотрудников' )
    for i,  sotrudnik in enumerate(spisok):
        if i == 0: 
            print(" ",sotrudnik)
        else:
            print(i,sotrudnik)



def add_employees():
    print('Введите Фамилию Имя Телефон и Должность через пробел: ')
    data = input().split()
    return data 


def change_employess():
    print('Выберете строчку для перезаписи: ')
    change = int(input())
    print('Введите строку для записи: ')
    string = input().split()
    return change, string 


def delete():
    print('напишите номер стороки для удаления: ')
    number = int(input())
    return number