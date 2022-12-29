'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''

import requests

url = 'http://numbersapi.com/'

def req_web(line):
    link = url + line+ '/math'
    params = {
    'json' : True,
    'math' : ''
    }
    r = requests.get(link, params=params)

    js = r.json()
    type_num = js['found']

    return type_num

with open('dataset_24476_3.txt', 'r') as f:
    for line in f:
        line = line.rstrip()

        type_num = req_web(line)

        if type_num:
            print('Interesting')
        else:
            print('Boring')
#
