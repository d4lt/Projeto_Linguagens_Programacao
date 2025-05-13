from flask import Flask, render_template, redirect, request
from pokemon_fetch import get_pokemon_data
from constants.pokemon_names import RND_POKEMON_NAMES
import random

app = Flask(__name__)

@app.route('/')
def home():
    searched_pokemon = request.args.get('search_pokemon')
    if searched_pokemon:
        pokemon = searched_pokemon
    else:
        random_pokemon = random.choice(RND_POKEMON_NAMES)
        pokemon = random_pokemon
        
    return redirect(f"/{pokemon}")

@app.route('/<string:pokemon_name>', methods=['GET'])
def show_pokemon(pokemon_name):
    try:
        pk_base_stats, pk_pokedex_data, pk_image = get_pokemon_data(pokemon_name)
    except Exception as e:
        raise Exception('Error when fetching from PokeAPI:', e)
    
    return render_template("pokemon.html", pokemon_name=pokemon_name, base_stats=pk_base_stats, pokedex_data=pk_pokedex_data, pokemon_image_link=pk_image)

if __name__ == '__main__':
    app.run(debug=True)