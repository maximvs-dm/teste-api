from flask import Flask
import requests

app = Flask(__name__)

bairros_atendidos = ['bom retiro', 'butantã', 'barra funda']


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/meu-bairro/<cep>")
def new_route(cep):
    print(f'O CEP digitado foi: {cep}')
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resp = requests.get(url)
    resp_dict = resp.json()
    bairro = resp_dict.get('bairro')

    if bairro is None:
        return "Bairro não encontrado", 404

    if bairro.lower() not in bairros_atendidos:
        return f"Bairro {bairro} não atendido"

    return f'Atendemos no bairro {bairro}'


@app.route("/not-found")
def not_found():
    return "Página não encontrada", 404
