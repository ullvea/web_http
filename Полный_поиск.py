import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

from get_size import get_size

# Пусть наше приложение предполагает запуск:
# python Полный_поиск.py Москва, ул. Ак. Королева, 12
toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "f86828c6-788e-41e3-bdfe-9f45d8f7ca92",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")


address_ll = ",".join([toponym_longitude, toponym_lattitude])
response = get_size(json_response, address_ll)



im = BytesIO(response.content)
opened_image = Image.open(im)
opened_image.show()  # Создадим картинку и тут же ее покажем встроенным просмотрщиком операционной системы
