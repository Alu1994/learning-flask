from app import app
from flask import render_template, redirect, url_for, flash, request

@app.route("/", defaults={"nome":"usuario", "profissao":"motorista", "github":"nao tenho"})
@app.route("/index", defaults={"nome":"usuario", "profissao":"motorista", "github":"nao tenho"})
@app.route("/index/<nome>/<profissao>/<github>")
def index(nome, profissao, github):
    dados = { "Nome": nome, "Profissao": profissao, "GitHub": github }
    return render_template('index.html', dados=dados)

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/autenticar", methods=['GET', 'POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == 'senha123':        
        return redirect(url_for('/login', usuario=usuario, senha=senha))
    else:
        flash("Dados invalidos")
        flash("Login ou Senha invalidos")
        return redirect('/login')