import view
import models
import logging


logging.basicConfig(
     filename='log_file.log',
     level=logging.INFO, 
     format='[%(asctime)s] %(name)s %(levelname)s %(message)s',
     datefmt='%H:%M:%S',
     encoding='utf-8',
 )

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)

logging.getLogger('').addHandler(console)


def main():
    select = view.show_menu()
    if select == 1:
        logging.info("Выбран 1")
        sotr = models.get_lists()
        view.show_employees(sotr)
    elif select == 2:
        logging.info("Выбран 2")
        data = view.add_employees()
        models.add_employess_to_list(data)
    elif select == 3:
        logging.info("Выбран 3")
        change, string = view.change_employess()
        models.update_employess(change, string)
    elif select == 4:
        logging.info("Выбран 4")
        number = view.delete()
        models.delets(number)
    elif select == 5:
        logging.info("Выбран 5")
        models.import_csv_function()
    elif select == 6:
        logging.info("Выбран 6")
        models.export_csv_function()

logging.info("Программа работает корректно")
    