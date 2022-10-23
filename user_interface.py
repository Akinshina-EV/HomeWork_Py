def get_number_menu():
    print('\nДобро пожаловать в базу данных (БД)\n'
          '"Успеваемость в начальной школе".\n'
          '\nВыберете пункт меню:\n'
          '\n1 - Показать все записи в БД.\n'
          '2 - Редактировать запись в БД.\n'
          '3 - Добавить запись в БД.\n'
          '4 - Удалить запись в БД.\n'
          '5 - Закрыть БД.\n')
    number_menu = input('Введите порядковый номер пункта меню: ')
    return number_menu


def get_student_new_grade():
    search_id = int(input('Введите номер строки, оценку в которой необходимо '
                          'изменить: '))
    new_grade = int(input('Введите новое значение "Grade": '))
    return search_id, new_grade


def get_stud_param():
    surname = input('Введите фамилию ученика: ')
    name = input('Введите имя ученика: ')
    year_of_study = input('Введите год обучения ученика: ')
    class_name = input('Введите литеру класса, в котором обучается ученик: ')
    return surname, name, year_of_study, class_name


def get_grade(lesson):
    grade = input(
        f'Введите оценку ученика по предмету {lesson}: ')
    return grade


def get_stud_for_del():
    stud_for_del = int(input('Введите значение "Student_id" ученика, запись о '
                             'котором необходимо удалить: '))
    return stud_for_del


def good_bay():
    print('До свиданья!')


def print_error():
    print('\nТакого пункта меню не существует.'
          '\nВведите цифру, соответствующую пункту меню.')
