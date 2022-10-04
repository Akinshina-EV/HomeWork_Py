def get_list_int():
    input_lst = input(
        'Введите список, состоящий из нескольких натуральных чисел:\n').split()
    result_list = []
    for i in input_lst:
        result_list.append(int(i))
    print(f'Исходный список:\n{result_list}')
    return result_list


def arithmetic_rounding(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
