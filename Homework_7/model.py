import csv

def import_txt_function():
    with open('import_file.txt', encoding='UTF-8') as file:
        lst = [line.rstrip() for line in file]
        filtered_list = list(filter(lambda x: x != '' , lst))
        converted_list = [filtered_list[i : i + 3] for i in range(0, len(filtered_list), 3)]
    print(f"Данные для справочника импортированы  из файла import_file.txt \n {converted_list} \n")
    return converted_list


def import_csv_function():
    lst = []
    with open("import_file.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            lst.append(row)
    print(f"Данные для справочника импортированы  из файла import_file.csv \n {lst} \n")
    return lst


def export_txt_function(data):
    with open('export_file.txt', 'w', encoding='UTF-8') as file:
        for item in data:
            for j in item:
                file.write(str(j) + '\n')
            file.write('\n')
    print(f"Данные справочника экспортированы в файл export_file.txt \n {data} \n")


def export_csv_function(data):
    with open("export_file.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        for row in data:
            file_writer.writerow(row)
    print(f"Данные справочника экспортированы в файл export_file.csv \n {data} \n")