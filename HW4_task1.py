# Вычислить число c заданной точностью d
#
#     Пример:
#
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)


from decimal import Decimal

number = Decimal(input('Введите вещественное число:\n'))
rounding_accuracy = input(f'Введите точность округления числа {number}\n'
                          f'из диапазона: 10^(-1) ≤ d ≤ 10^(-10): \n')
rounding_accuracy.replace('1', '0').replace('0', '1', 1)
print(
    f'Число {number} с заданной точностью {rounding_accuracy}: \n'
    f'{number.quantize(Decimal(rounding_accuracy))}')
