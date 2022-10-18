import os.path
import phonebook_utils as func


def menu():
    while True:
        print('\nВас приветствует Телефонный справочник.\n'
              '\nВыберете пункт меню:\n'
              '\n1 - Показать все записи в телефонном справочнике.\n'
              '2 - Найти запись в справочнике по имени.\n'
              '3 - Найти запись в справочнике по фамилии.\n'
              '4 - Найти запись в справочнике по дате рождения.\n'
              '5 - Найти запись в справочнике по месту работы.\n'
              '6 - Поиск записи в справочнике по номеру телефона.\n'
              '7 - Добавить новую запись.\n'
              '8 - Закрыть телефонный справочник.\n')
        number_menu = input('Введите порядковый номер пункта меню: ')

        if number_menu.isdigit() and int(number_menu) in range(1, 9):
            result_print = []

            if int(number_menu) == 1:
                if os.path.exists('phonebook.csv'):
                    result_print = func.read_phonebook()
                else:
                    count = int(input('Задайте необходимое количество строк в '
                                      'телефонном справочнике: '))
                    result_print = func.create_phonebook(count)

            elif int(number_menu) == 2:
                search_name = input('Введите имя: ')
                result_print = func.search_phonebook(name=search_name)

            elif int(number_menu) == 3:
                search_surname = input('Введите фамилию: ')
                result_print = func.search_phonebook(surname=search_surname)

            elif int(number_menu) == 4:
                search_birthday = input('Введите дату рождения: ')
                result_print = func.search_phonebook(birthday=search_birthday)

            elif int(number_menu) == 5:
                search_work_place = input('Введите место работы: ')
                result_print = func.search_phonebook(
                    work_place=search_work_place)

            elif int(number_menu) == 6:
                search_number = input('Введите номер телефона: ')
                result_print = func.search_phonebook(
                    phone_number=search_number)

            elif int(number_menu) == 7:
                name = input('Введите имя: ')
                surname = input('Введите фамилию: ')
                birthday = input('Введите дату рождения: ')
                work_place = input('Введите место работы: ')
                phone_number = input('Введите номер телефона: ')
                result_print = func.add_row_phonebook(name, surname, birthday,
                                                      work_place, phone_number)

            elif int(number_menu) == 8:
                print('До свиданья!')
                break

            [print(f'{" ".join(row)}\n') for row in result_print if row]

        else:
            print(
                '\nТакого пункта меню не существует.\n'
                'Введите цифру, соответствующую пункту меню.')
