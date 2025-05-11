import requests
import json



def get_pokemon_data(pokemon_name: str) -> list:
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if r.status_code == 200:
        data = r.json()
        
        base_stats = {}
        stats = data['stats']
        for s in stats:
            name = s['stat']['name']
            base_stats[name] = s['base_stat']
            
        pokedex_data =  { 
                        'id': data['id'],
                        'types': [pk_type['type']['name'] for pk_type in data['types']],
                        'height': data['height'] / 10,
                        'weight': data['weight'] / 10,
                        'abilities': [ability['ability']['name'] for ability in data['abilities']]
                        }
        

        return [base_stats, pokedex_data]
    else:
        raise Exception("Error fetching data from PokeAPI: Wrong Pokemon name")