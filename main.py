from asyncio.base_events import Server
from atexit import register
#from crypt import methods
from distutils.log import Log
from http import server
from flask import Flask,render_template,flash,redirect,url_for,request
from flask_login import LoginManager, login_user,logout_user
from flask_sqlalchemy import SQLAlchemy
import models
import consulta
import locale



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dash_db'
login_manager = LoginManager(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '2qybcjqw'



@login_manager.user_loader
def load_user(user_id):
    return models.User.get(user_id)


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

    ranking = consulta.RkVendedores()
    for posicao in ranking:
        vendedor = []
        totalvd = []
        vendedor.append(posicao[0])
        totalvd.append(posicao[1])    

    return render_template('index.html', peso=pesovendido,vendas=vendido,nvendas=qtd_vendido, canceladas=qtd_canceladas
                            ,percent_cancel = perc_cancel
                            ,tx_convert = tx_conversao
                            ,vendedor = vendedor
                            ,totalvd = totalvd
                            ,rank = ranking)



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = models.User.query.filter_by(email=email).frist()

        if not user or not verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('/'))

    return render_template('login.html')


@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))



app.run(host="0.0.0.0",port=7000)