from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/pokeresult', methods=['POST'])
def pokedata():
    num = request.form['pokeq']
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+num+'/')
    json_object = r.json()
    poke_id = json_object ['id']
    poke_name = json_object ['name']
    poke_pic = json_object ['sprites'] ['front_default']
    poke_peso = json_object ['weight']
    return render_template('pokeresult.html', pokeid=poke_id, pokename=poke_name, pokepic=poke_pic, pokepeso=poke_peso)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)