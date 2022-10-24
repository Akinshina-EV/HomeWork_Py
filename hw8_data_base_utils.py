import pandas

import hw8_user_interface as ui
from hw8_data_base import (
    DATA_PROGRESS, DATA_STUDENT, TITLE_DATA_PROGRESS,
    TITLE_DATA_STUDENT,
)

PATH1 = 'data_student.csv'
PATH2 = 'data_progress.csv'

LESSONS = ['Математика', 'Русский язык', 'Литература']


def get_data_base():
    """Создает БД при первом вызове программы"""
    df_student = pandas.DataFrame(DATA_STUDENT, columns=TITLE_DATA_STUDENT)
    df_progress = pandas.DataFrame(DATA_PROGRESS, columns=TITLE_DATA_PROGRESS)
    df_student.to_csv(PATH1, index=False)
    df_progress.to_csv(PATH2, index=False)
    return get_result_data_base()


def read_data_base(path):
    """Импортирует файл csv в Data Frame"""
    df = pandas.read_csv(path)
    return df


def merge_data_base(data1, data2):
    """Объединяет две таблицы БД"""
    data = pandas.merge(data1, data2, how='outer', on='Student_id')
    return data


def get_result_data_base():
    """Считывает данные двух таблиц БД и объединяет их, если таблицы были
    созданы ранее"""
    df1 = read_data_base(PATH1)
    df2 = read_data_base(PATH2)
    return merge_data_base(df1, df2)


def change_data_base():
    """Изменяет оценку ученика по выбранному предмету"""
    search_id, new_grade = ui.get_student_new_grade()
    df_progress = read_data_base(PATH2)
    df_progress.loc[df_progress.index == search_id, 'Grade'] = new_grade
    df_progress.to_csv(PATH2, index=False)
    return get_result_data_base()


def add_row_data_student():
    """Добавляет ученика в БД"""
    params = ui.get_student_param()
    df_student = read_data_base(PATH1)
    df_student.loc[len(df_student.index)] = [
        df_student['Student_id'].max() + 1, *params]
    df_student.to_csv(PATH1, index=False)
    return df_student['Student_id'].max(), df_student


def add_row_data_progress(student_id, grades):
    """Добавляет информацию в БД об успеваемости ученика"""
    df_progress = read_data_base(PATH2)
    for i, lesson in enumerate(LESSONS):
        df_progress.loc[len(df_progress.index)] = [student_id, lesson,
                                                   grades[i]]
    df_progress.to_csv(PATH2, index=False)
    return df_progress


def del_row_from_db(path, student_id):
    """Удаляет информацию из БД об ученике"""
    data_frame = read_data_base(path)
    data_frame = data_frame[data_frame.Student_id != student_id]
    data_frame.to_csv(path, index=False)
    return data_frame
