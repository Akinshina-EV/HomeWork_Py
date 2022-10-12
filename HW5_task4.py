# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


import itertools


def read_file(path):
    with open(path, 'r') as f:
        txt = f.read()
    return txt


path1 = 'text_5_4.txt'
path2 = 'text_5_4_rle.txt'
text = read_file(path1)
print(f'Исходный текст:\n\n{text}\n')

text_rle = ''
for symbol, symbol_list in itertools.groupby(text):
    symbol_count = sum(1 for _ in symbol_list)
    text_rle += str(symbol_count) + symbol
with open(path2, 'w', encoding='utf-8') as data:
    data.write(text_rle)
text_rle_read = read_file(path2)
print(f'Закодированный текст:\n\n{text_rle_read}')

text_decode = ''
count = 0
for item in text_rle_read:
    if item.isdigit:
        count += int(item)
    else:
        text_decode += item * count
        count = 0
print(text_decode)




# #
# def rle_decode(string: str):
#     decode_string = ''
#     i = 0
#     while len(string[i: i + 2]) == 2:
#         num, char = string[i: i + 2]
# #         decode_string += char * int(num)
# #         i += 2
# #         return decode_string
