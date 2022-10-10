# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


from itertools import groupby
import itertools

with open('text.txt', 'r') as f:
    text = f.read()
print(f'Исходный текст:\n\n{text}\n')

text_tuple = [(symbol, len(list(symbol_lst))) for symbol, symbol_lst in groupby(text)]


text_lst = [str(item) for item in itertools.chain(*text_tuple)]
text_zip = ''.join(text_lst)
print(text_zip)
