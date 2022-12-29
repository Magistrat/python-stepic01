'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
'''

import csv
dict_def = dict()

def dict_ct(val, dict_def):
    if val not in dict_def.keys():
        dict_def[val] = 1

    dict_def[val] = dict_def[val] + 1

with open ("Crimes.csv", "r") as c:
    cs = csv.reader(c)
    for row in cs:
        data = row[2]
        data = data.split('/')[-1].split(' ')[0]
        if data == "2015":
            val = row[5]
            dict_ct(val, dict_def)

print(dict_def) #THEFT
