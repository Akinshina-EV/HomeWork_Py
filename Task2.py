# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def get_predicate(x):
    print(f'Введите значение {x}:')
    x = input()
    return x


x = get_predicate('X')
y = get_predicate('Y')
z = get_predicate('Z')
left = not (x or y or z)
right = not x and not y and not z
if left == right:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
