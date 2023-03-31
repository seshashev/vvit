import requests
city = 'Moscow,RU'
appid = input('Введите ваш API-ключ: ')
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q':city, 'units':'metric', 'lang': 'ru', 'APPID':appid})
data = res.json()
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                 params={'q':city, 'units':'metric', 'lang': 'ru', 'APPID':appid})
data = res.json()
print("Скорость на неделю:")
print(res.url)
for i in data['list']:
    print("Скорость ветра:", i['wind']['speed'])
    print("Видимость:", i['visibility'])
    print("________________")
