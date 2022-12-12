
'''

Вам дана в архиве (https://stepik.org/media/attachments/lesson/24465/main.zip) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

'''



import os
import os.path
end = []
# Папка 'main' должна быть рядом
for cur_path, dirs, files in os.walk('main'):
    for file in files:
        if file.endswith('.py'):
            if cur_path not in end:
                end.append(cur_path)
end.sort()
with open('end.txt', 'w') as w:
    save = '\n'.join(end)
    w.write(save)
