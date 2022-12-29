'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

Работа с API Artsy
Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.
Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.
После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.
'''

import requests
import json

'''client_id = '8a81785d931f78c8bda0'
client_secret = 'c455f56b588421464bd0c02e6fb93dbf'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
'''
token = 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2M2FkZjhmODU1OTFhNDAwMGMzZjQ1ZDgiLCJleHAiOjE2NzI5NTA2NDksImlhdCI6MTY3MjM0NTg0OSwiYXVkIjoiNjNhZGY4Zjg1NTkxYTQwMDBjM2Y0NWQ4IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYzYWRmOGY5MDUwNzY4MDAwZGVhYTVhOCJ9.hgziozSqnlSmJQAqvR3PegrbYbmz4j9xm9txL84rs4Y'
link = 'https://api.artsy.net/api/artists/'

dict_end = dict()
pr_ar = []
year_ar = []

def dict_make(name, year):
    dict_end[year] = name

def req_art(key):
    headers = {"X-Xapp-Token" : token}
    r = requests.get(link + key, headers=headers)
    j = r.json()
    year = j['birthday']
    name = j['name']
    dict_make(name, year)
    year_ar.append(year)





with open('dataset_24476_4.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        req_art(line)


year_ar.sort()
for ye in year_ar:
    pr_ar.append(dict_end[ye])


# print(pr_ar)
# print(dict_end)

for pr in pr_ar:
    print(pr)
#
