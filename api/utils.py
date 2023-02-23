import requests

api_base_url = "https://pokeapi.co/api/v2/pokemon/"
headers = {'Accept': 'application/json'}


def request_pokeapi(url: str):
    return requests.get(url, headers=headers)


def request_all_pokemon():
    return requests.get(api_base_url, headers=headers)


def request_pokemon_by_id(id: str):
    return requests.get(api_base_url + id, headers=headers)


def request_pokemon_by_name(name: str):
    return requests.get(api_base_url + name, headers=headers)
