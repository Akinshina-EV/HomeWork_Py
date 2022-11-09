import csv
from utils import row_creation


def read_phonebook():
    phonebook = []
    with open('phonebook.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            phonebook.append(row)
        return phonebook


def add_row_phonebook(name, surname, birthday, work_place, phone_number):
    phonebook = read_phonebook()
    last_row = int(phonebook[-2][0])
    new_row = [str(last_row + 1), name.title(),
               surname.title(), birthday, work_place, phone_number]
    with open('phonebook.csv', 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_row)
        writer.writerow('')
    return [new_row]


def search_phonebook(name='', surname='', birthday='', work_place='',
                     phone_number=''):
    result = []
    for row in read_phonebook():
        if row and any([row[1] == name, row[2] == surname, row[3] == birthday,
                        row[4] == work_place, phone_number in row[5].split()]):
            result.append(row)
    if not result:
        print('Контакты не найдены')
    return result


def create_phonebook(count):
    with open('phonebook.csv', 'w+', newline='', encoding='utf-8') as csv_file:
        title = ['ID', 'Имя', 'Фамилия', 'День рождения', 'Место работы',
                 'Номер телефона']
        writer = csv.writer(csv_file)
        writer.writerow(title)
        writer.writerow('')
        for i in range(1, count + 1):
            row = row_creation()
            row.insert(0, i)
            writer = csv.writer(csv_file)
            writer.writerow(row)
            writer.writerow('')
    return read_phonebook()
