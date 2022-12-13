# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ' )

del_text = 'абв'

result = ' '.join(filter(lambda x: del_text not in x, text.split()))
print(result)