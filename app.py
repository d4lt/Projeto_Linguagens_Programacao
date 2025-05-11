from flask import Flask, render_template
from pokemon_fetch import get_pokemon_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/<string:pokemon_name>', methods=['GET'])
def show_pokemon(pokemon_name):
    try:
        pk_base_stats, pk_pokedex_data = get_pokemon_data(pokemon_name)
    except Exception as e:
        raise Exception('Error when fetching from PokeAPI:', e)
    
    return render_template("pokemon.html", pokemon_name=pokemon_name, base_stats=pk_base_stats, pokedex_data=pk_pokedex_data)

if __name__ == '__main__':
    app.run(debug=True)