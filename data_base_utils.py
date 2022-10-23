import pandas

from data_base import (
    DATA_PROGRESS, DATA_STUDENT, title_data_progress,
    title_data_student,
)

PATH1 = 'data_student.csv'
PATH2 = 'data_progress.csv'

lesson = ['Математика', 'Русский язык', 'Литература']


def get_data_base():
    df_student = pandas.DataFrame(DATA_STUDENT, columns=title_data_student)
    df_progress = pandas.DataFrame(DATA_PROGRESS, columns=title_data_progress)
    df_student.to_csv(PATH1, index=False)
    df_progress.to_csv(PATH2, index=False)
    return get_result_data_base()


def read_data_base(path):
    df = pandas.read_csv(path)
    return df


def merge_data_base(data1, data2):
    data = pandas.merge(data1, data2, how='outer', on='Student_id')
    return data


def get_result_data_base():
    df1 = read_data_base(PATH1)
    df2 = read_data_base(PATH2)
    return merge_data_base(df1, df2)


def change_data_base(search_id, new_grade):
    df_progress = read_data_base(PATH2)
    df_progress.loc[df_progress.index == search_id, 'Grade'] = new_grade
    df_progress.to_csv(PATH2, index=False)
    return get_result_data_base()


def add_row_data_student(surname, name, year_of_study, class_name):
    df_student = read_data_base(PATH1)
    df_student.loc[len(df_student.index)] = [
        df_student['Student_id'].max() + 1,
        surname, name, year_of_study,
        class_name]
    df_student.to_csv(PATH1, index=False)
    return df_student['Student_id'].max(), df_student


def add_row_data_progress(student_id, grade):
    df_progress = read_data_base(PATH2)
    for i, les in enumerate(lesson):
        for j, gr in enumerate(grade):
            if i == j:
                df_progress.loc[len(df_progress.index)] = [student_id, les, gr]
    df_progress.to_csv(PATH2, index=False)
    return df_progress


def del_row_data_base(student_id):
    df_student = read_data_base(PATH1)
    df_student = df_student[df_student.Student_id != student_id]
    df_student.to_csv(PATH1, index=False)
    df_progress = read_data_base(PATH2)
    df_progress = df_progress[df_progress.Student_id != student_id]
    df_progress.to_csv(PATH2, index=False)
    return df_student, df_progress
