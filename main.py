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
    if vd == None:
        vd = 0
    else:
        vd = consulta.ValorVendido()
    vendido = locale.currency(vd, grouping=True)
    if vendido:
        pass
    else:
        vendido = 0
        
    qtd_vendido = consulta.QtdVendas()
    if qtd_vendido:
        pass
    else:
        qtd_vendido = 0

    qtd_canceladas = consulta.QtdCanceladas()
    if qtd_vendido == 0:
        qtd_canceladas = 0
        perc_cancel = 0
    else:
        qtd_canceladas = consulta.QtdCanceladas()
        perc_cancel = (qtd_canceladas * 100) / qtd_vendido
        perc_cancel = round(perc_cancel,2)
    #Taxa de Conversao
    if qtd_vendido == 0:
        tx_conversao = 0
        nvendido = 0
    else:
        nvendido = consulta.QtdNaoVendido()
        tx_conversao = ((qtd_vendido / nvendido) * 100)
        tx_conversao = round(tx_conversao)
    return render_template('index.html', peso=pesovendido,vendas=vendido,nvendas=qtd_vendido, canceladas=qtd_canceladas
                            ,percent_cancel = perc_cancel
                            ,tx_convert = tx_conversao)

app.run(host="0.0.0.0",port=7000)