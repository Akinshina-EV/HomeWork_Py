#     Напишите программу, которая принимает на вход координаты двух точек
#     и находит расстояние между ними в 2D пространстве.
#
#     Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def get_coordinate(point, x):
    coordinate_name = ['x', 'y']
    coordinate_point = []
    for i in range(x):
        coordinate = int(input(f'Введите координаты точки {point} по оси {coordinate_name[i]}: '))
        coordinate_point.append(coordinate)
    return coordinate_point


a = get_coordinate('A', 2)
b = get_coordinate('B', 2)
length_ab = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (1/2)
print(f'Расстояние между точками A и B: {round(length_ab, 2)}')