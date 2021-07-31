import json
import requests
import time

from cachetools import cached, TTLCache
cache = TTLCache(maxsize=100, ttl=300)
array = []


@cached(cache)
def getting_weather_data(city_id):
    res = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?id={id}&units=metric&appid=9a2f57a94f70ed16f3511c1d48f83e33"
        .format(id=city_id))
    time.sleep(5)
    return res


with open('cities.json', encoding='utf-8') as my_city:
    my_cities = json.loads(my_city.read())
    for city_data in range(len(my_cities['List'])):
        array.append(my_cities['List'][city_data]['CityCode'])


print("these are your city codes:-----------")
print(array)


while True:
    x = input("\n Input your city ID:-")
    print(getting_weather_data(x).status_code)
    responce_dic = getting_weather_data(x).json()
    print("contry      : {}".format(responce_dic['sys']['country']))
    print("sunrice     : {}".format(responce_dic['sys']['sunrise']))
    print("sunset      : {}".format(responce_dic['sys']['sunset']))
    print("main        : {}".format(responce_dic['weather'][0]['main']))
    print("description : {}".format(responce_dic['weather'][0]['description']))
    print("temp        : {}".format(responce_dic['main']['temp']))
    print("pressure    : {}".format(responce_dic['main']['pressure']))
    print("humidity    : {}".format(responce_dic['main']['humidity']))
    print("temp_max    : {}".format(responce_dic['main']['temp_max']))
    print("temp_min    : {}".format(responce_dic['main']['temp_min']))
    print("visibility  : {}".format(responce_dic['visibility']))
    print("wind        : {}".format(responce_dic['wind']['speed']))
    print("deg         : {}".format(responce_dic['wind']['deg']))
    print("all         : {}".format(responce_dic['clouds']['all']))
    print("dt          : {}".format(responce_dic['dt']))
    print("id          : {}".format(responce_dic['id']))
    print("name        : {}".format(responce_dic['name']))
