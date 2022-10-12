# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


with open('text.txt', 'r') as f:
    text = f.read()
print(f'Исходный текст:\n\n{text}\n')
text_lst = text.replace('.', ' .').replace(',', ' ,').split()
fragments = ['а', 'б', 'в']
result_lst = []
for word in text_lst:
    if any([fragment not in word.casefold() for fragment in fragments]):
        result_lst.append(word)
print(
    f'Отформатированный текст, из которого удалены все слова, содержащие '
    f'"абв":\n\n{" ".join(result_lst).replace(" .", ".").replace(" ,", ",")}')
