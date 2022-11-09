def get_list(mark=True):
    number_type = '' if mark else 'вещественных'
    count = int(input(f'Задайте длину списка, состоящего из {number_type} '
                      f'чисел: '))
    input_lst = []
    for i in range(1, count + 1):
        input_number = input(
            f'Введите {i} {number_type} элемент списка: ')
        input_lst.append(input_number)
    if mark:
        result_list = [int(i) for i in input_lst]
    else:
        result_list = [float(i) for i in input_lst]
    print(f'Исходный список:\n{result_list}')
    return result_list


def arithmetic_rounding(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
