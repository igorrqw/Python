from view import hello_function
from view import get_type_import
from view import get_type_export
from model import import_txt_function
from model import import_csv_function
from model import export_txt_function
from model import export_csv_function


def main_function():
    phonebook = [
        ['Иванов', 'Иван', 8797987],
        ['Петров','Петр',32445432],
        ['Сидоров','Иван',23423432]
    ]

    hello_function(phonebook)

    type_import = get_type_import()

    if type_import == 1:
        phonebook = import_txt_function()
    elif type_import == 2:
        phonebook = import_csv_function() 


    type_export = get_type_export()

    if type_export == 3:
        export_txt_function(phonebook)
    elif type_export == 4:
        export_csv_function(phonebook)