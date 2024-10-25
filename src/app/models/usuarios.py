from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from .tables import Usuario
from app import db

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates", static_folder="static")

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuarios_create.html')
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        
        u = Usuario(nome, email, senha)
        db.session.add(u)
        db.session.commit()
        
        # return '<a href="/usuarios/recovery">index</a></br>Dados cadastrados com sucesso'
        return redirect('/usuarios/recovery')

@bp_usuarios.route('/recovery', methods=['GET'])
def recovery():
    if request.method == 'GET':
        usuarios = Usuario.query.all()
        return render_template('usuarios_recovery.html', usuarios=usuarios)
    
@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    usuario = Usuario.query.get(id)
    
    if request.method == 'GET':
        return render_template('usuarios_update.html', usuario=usuario)
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        usuario.nome = nome
        usuario.email = email
        
        db.session.add(usuario)
        db.session.commit()
        
        # return '<a href="/usuarios/recovery">index</a></br>Dados atualizados com sucesso'
        return redirect('/usuarios/recovery')

@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    usuario = Usuario.query.get(id)
    
    if request.method == 'GET':
        return render_template('usuarios_delete.html', usuario=usuario)
    
    if request.method == 'POST':
        db.session.delete(usuario)
        db.session.commit()
        
        # return '<a href="/usuarios/recovery">index</a></br>Dados atualizados com sucesso'
        return redirect('/usuarios/recovery')