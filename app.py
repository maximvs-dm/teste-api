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


@app.route("/listar")
def lista_bairros():
    return bairros_atendidos


@app.route("/adicionar/<novo_bairro>")
def add_bairro(novo_bairro):
    bairros_atendidos.append(novo_bairro.lower())
    return 'ok'


@app.route("/remover/<bairro>")
def remove_bairro(bairro):
    try:
        bairros_atendidos.remove(bairro.lower())
    except ValueError:
        return 'bairro não encontrado'
    except Exception:
        return 'erro desconhecido'
    else:
        return 'ok'
