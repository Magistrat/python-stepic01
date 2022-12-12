'''

Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab

'''
end = []

# Нужно вставить dataset в папку с кодом
with open('dataset_24465_4.txt', 'r') as f, open('end.txt', 'w') as w:
    for line in f:
        line = line.rstrip()
        end.append(line)
    end = end[::-1]
    content = '\n'.join(end)
    w.write(content)
