import csv


def read_phonebook():
    phonebook = ''
    for row in list_phonebook():
        phonebook += ' '.join(row) + '\n'
    return phonebook


def list_phonebook():
    with open('phonebook.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        return [row for row in reader]


def add_row_phonebook(name, surname, phone_number):
    phonebook = list_phonebook()
    last_row = 0 if phonebook[-1][0] == 'ID' else int(phonebook[-1][0])
    new_row = [str(last_row + 1), name.title(), surname.title(), phone_number]
    with open('phonebook.csv', 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_row)
    return new_row


def create_phonebook():
    with open('phonebook.csv', 'w+', newline='', encoding='utf-8') as csv_file:
        title = ['ID', 'Имя', 'Фамилия', 'Номер телефона']
        writer = csv.writer(csv_file)
        writer.writerow(title)
    return read_phonebook()


def find_contact(find):
    result = ''
    for row in list_phonebook():
        if row and any([row[0] == find, row[1] == find.title(),
                        row[2] == find.title(), row[3] == find]):
            result += ' '.join(row) + '\n'
    return result


def deleted_contact(id_contact):
    result = [row for row in list_phonebook() if row[0] != id_contact]
    with open('phonebook.csv', 'w', newline='',
              encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        [writer.writerow(row) for row in result]
