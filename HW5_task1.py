# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


with open('text.txt', 'r') as f:
    text = f.read()
print(f'Исходный текст:\n\n{text}\n')
text_lst = text.replace('.', ' .').replace(',', ' ,').split()
fragment = ['а', 'б', 'в']
result_lst = []
for word in text_lst:
    if fragment[0] not in word.casefold() or fragment[1] not in \
            word.casefold() or fragment[2] not in word.casefold():
        result_lst.append(word)
print(
    f'Отформатированный текст, из которого удалены все слова, содержащие '
    f'"абв":\n\n{" ".join(result_lst).replace(" .", ".").replace(" ,", ",")}')
