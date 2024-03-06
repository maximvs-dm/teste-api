from flask import Flask
from errors import BairroNotFoundError
from request_helper import get_bairro

app = Flask(__name__)

bairros_atendidos = ['bom retiro', 'butantã', 'barra funda']


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/atende/<cep>")
def new_route(cep):
    try:
        bairro = get_bairro(cep)
    except BairroNotFoundError as e:
        print(e)
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
        return 'bairro não encontrado', 404
    except Exception:
        return 'erro desconhecido', 400
    else:
        return 'ok'
