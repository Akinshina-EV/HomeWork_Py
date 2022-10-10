# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


with open('text.txt', 'r') as f:
    text = f.read()
print(f'Исходный текст:\n\n{text}\n')
text_lst = text.replace('.', ' .').replace(',', ' ,').split()
fragment = 'абв'
result_lst = []
for word in text_lst:
    if fragment not in word.casefold():
        result_lst.append(word)
print(
    f'Отформатированный текст, из которого удалены все слова, содержащие '
    f'"абв":\n\n{" ".join(result_lst).replace(" .", ".").replace(" ,", ",")}')
