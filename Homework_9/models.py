from view import*
import csv


def show_employees(update, context):
    with open ('file.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        sp = list(reader)

    for i,  sotrudnik in enumerate(sp):
        if i == 0: 
            print(" ",sotrudnik)
            update.message.reply_text(''.join([str(element) for element in sotrudnik]))
        else:
            print(i,sotrudnik)
            update.message.reply_text(' '.join([str(element) for element in sotrudnik]))


def add_employess_to_list(update, context):
    employess = update.message.text
    employess = employess.split()
    employess.pop(0)

    with open ('file.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employess)


def find_employess(update, context):
    employe = update.message.text
    employe = employe.split()
    employe.pop(0)
    employe = ''.join(employe)

    with open ('file.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        sp = list(reader)
    
    for i,  sotrudnik in enumerate(sp):
        if (sotrudnik[0] == ''.join(employe)):
            update.message.reply_text(' '.join([str(element) for element in sotrudnik]))
        
    
def del_employess(update, context):
    employe = update.message.text
    employe = employe.split()
    employe.pop(0)
    employe = ''.join(employe)
    
    with open ('file.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        sp = list(reader)
    
    for i,  sotrudnik in enumerate(sp):
        if (sotrudnik[0] == ''.join(employe)):
            with open ('file.csv', 'r', encoding="utf8", newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                data = list(reader)
                del data[i]
            with open ('file.csv', 'w', encoding="utf8", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                for i in data:
                    writer.writerow(i)

            update.message.reply_text('Удалена запись: ')
            update.message.reply_text(' '.join([str(element) for element in sotrudnik]))