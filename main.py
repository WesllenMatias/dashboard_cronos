from asyncio.base_events import Server
from http import server
from flask import Flask, render_template
import pymssql
import consulta



app = Flask(__name__)


@app.route('/')
def home():

    pesovendido = consulta.PesoVendido()
    vendido = consulta.ValorVendido()
    return render_template('index.html', peso=pesovendido,vendas=vendido)
