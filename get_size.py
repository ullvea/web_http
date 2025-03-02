import requests

def get_size(json_response, adress_ll):
    print("Введите размеры объекта в градусной мере:")
    delta1 = input('[1]: ')
    delta2 = input('[2]: ')
    apikey = "e5e3e79c-5182-4afc-b1a9-c1ab82bfcad7"
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": adress_ll,
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "apikey": apikey,
        "pt": "{},comma".format(adress_ll)
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response