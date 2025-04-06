from flask import Flask
from pokemon import get_pokemon_data

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Search a Pokemon!</h1>'

@app.route('/<string:pokemon_name>', methods=['GET'])
def show_pokemon(pokemon_name):
    try:
        pokemon_abilities = get_pokemon_data(pokemon_name)
    except:
        raise Exception('(Probally) you typed the wrong pokemon name.')
    
    text = \
    f"<h1> \
    {pokemon_name} has the following abilities: {pokemon_abilities} \
    </h1>" \

    return text

if __name__ == '__main__':
    app.run(debug=True)