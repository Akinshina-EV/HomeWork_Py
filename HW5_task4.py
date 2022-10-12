# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


import itertools


def read_file(path1):
    with open(path1, 'r') as f:
        txt = f.read()
    return txt


def write_file(path2, texts):
    with open(path2, 'w', encoding='utf-8') as f:
        f.write(texts)


path_1 = 'text_5_4.txt'
path_2 = 'text_5_4_rle.txt'
path_3 = 'text_5_4_decode.txt'
text = read_file(path_1)
print(f'Исходный текст:\n\n{text}\n')

text_rle = ''
for symbol, symbol_list in itertools.groupby(text):
    symbol_count = len(list(symbol_list))
    text_rle += str(symbol_count) + symbol
write_file(path_2, text_rle)
text_rle_read = read_file(path_2)
print(f'Закодированный текст:\n\n{text_rle_read}')

text_decode = ''
count = 0
for item in text_rle_read:
    if item.isdigit():
        count += int(item)
    else:
        text_decode += item * count
        count = 0
write_file(path_3, text_decode)
text_recode = read_file(path_3)
print(f'\nДекодированный текст:\n\n{text_recode}')
