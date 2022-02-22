from asyncio.base_events import Server
from http import server
from flask import Flask, render_template
import pymssql
import consulta
import locale



app = Flask(__name__)


@app.route('/')
def home():
    locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')
    
    pesovendido = consulta.PesoVendido()
    vd = consulta.ValorVendido()
    vendido = locale.currency(vd, grouping=True)
    return render_template('index.html', peso=pesovendido,vendas=vendido)


app.run(host="0.0.0.0",port=5000)