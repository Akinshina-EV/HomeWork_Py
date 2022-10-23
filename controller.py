import os.path

import data_base_utils as dbu
import user_interface as ui


def menu():
    while True:
        number_menu = ui.get_number_menu()

        if number_menu.isdigit() and int(number_menu) in range(1, 6):
            if int(number_menu) == 1:
                if os.path.exists('data_student.csv') and os.path.exists(
                        'data_progress.csv'):
                    data_frame = dbu.get_result_data_base()
                else:
                    data_frame = dbu.get_data_base()
                print(data_frame)

            elif int(number_menu) == 2:
                search_id, new_grade = ui.get_student_new_grade()
                new_data_frame = dbu.change_data_base(search_id, new_grade)
                print(new_data_frame)

            elif int(number_menu) == 3:
                surname, name, year_of_study, class_name = ui.get_stud_param()
                student_id, df_student = dbu.add_row_data_student(surname,
                                                                  name,
                                                                  year_of_study,
                                                                  class_name)
                grades = []
                for les in dbu.lesson:
                    grade = ui.get_grade(les)
                    grades.append(grade)
                df_progress = dbu.add_row_data_progress(student_id, grades)
                add_data_frame = dbu.merge_data_base(df_student, df_progress)
                print(add_data_frame)

            elif int(number_menu) == 4:
                stud_for_del = ui.get_stud_for_del()
                new_df_stud, new_df_progress = dbu.del_row_data_base(
                    stud_for_del)
                new_data_frame = dbu.merge_data_base(new_df_stud,
                                                     new_df_progress)
                print(new_data_frame)

            elif int(number_menu) == 5:
                ui.good_bay()
                break

        else:
            ui.print_error()
