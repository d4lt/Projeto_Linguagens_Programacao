import requests
import json



def get_pokemon_data(pokemon_name: str) -> list:
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if r.status_code == 200:
        abilities_names = []
        data = r.json()
        abilities = data['abilities']
        for ability in abilities:
            abilities_names.append(ability['ability']['name'])

        return abilities_names
    else:
        raise Exception("Error fetching data from PokeAPI")