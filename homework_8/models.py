import csv
import logging


def get_lists():
    with open ('file.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        return list(reader)


def add_employess_to_list(employess):
    with open ('file.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employess)


def update_employess(number, string):
    try:
        with open ('file.csv', 'r', encoding="utf8", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string 
        with open ('file.csv', 'w', encoding="utf8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        logging.error(f'Вы вышли за границы массива, введена неверная строка для перезаписи: {number}')
        exit()
    


def delets(number):
    with open ('file.csv', 'r', encoding="utf8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open ('file.csv', 'w', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)
    logging.info(f'Удалена запись на строке: {number}')


def import_csv_function():
    with open("import_file.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            add_employess_to_list(row)
    logging.info(f"Данные для справочника импортированы из файла 'import_file.csv' в 'file.csv'")


def export_csv_function():
    lst = []
    with open("file.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader: 
            lst.append(row)
    with open("export_file.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        for row in lst:
            file_writer.writerow(row)
    logging.info(f"Данные справочника экспортированы в файл 'export_file.csv'") 
