import os.path

import hw8_data_base_utils as dbu
import hw8_user_interface as ui


def menu():
    while True:
        menu_number = ui.get_number_menu()

        if menu_number.isdigit() and int(menu_number) in range(1, 6):
            if int(menu_number) == 1:
                if os.path.exists('data_student.csv') and os.path.exists(
                        'data_progress.csv'):
                    data_frame = dbu.get_result_data_base()
                else:
                    data_frame = dbu.get_data_base()
                print(data_frame.to_markdown())

            elif int(menu_number) == 2:
                print(dbu.change_data_base().to_markdown())

            elif int(menu_number) == 3:
                student_id, df_student = dbu.add_row_data_student()
                grades = []
                for les in dbu.LESSONS:
                    grade = ui.get_grade(les)
                    grades.append(grade)
                df_progress = dbu.add_row_data_progress(student_id, grades)
                add_data_frame = dbu.merge_data_base(df_student, df_progress)
                print(add_data_frame.to_markdown())

            elif int(menu_number) == 4:
                student_id = ui.get_stud_for_del()
                new_df_stud = dbu.del_row_from_db(dbu.PATH1, student_id)
                new_df_progress = dbu.del_row_from_db(dbu.PATH2, student_id)
                new_data_frame = dbu.merge_data_base(new_df_stud,
                                                     new_df_progress)
                print(new_data_frame.to_markdown())

            elif int(menu_number) == 5:
                ui.good_buy()
                break

        else:
            ui.print_error()
