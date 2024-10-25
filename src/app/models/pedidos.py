from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from .tables import Pedido
from app import db
from datetime import datetime

bp_pedidos = Blueprint("pedidos", __name__, template_folder="templates", static_folder="static")

@bp_pedidos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('pedidos_create.html')
    
    if request.method == 'POST':
        usuario_id = request.form.get('usuario_id')
        pizza_id = request.form.get('pizza_id')
        data = datetime.today()
        
        pedido = Pedido(usuario_id, pizza_id, data)
        db.session.add(pedido)
        db.session.commit()
        
        return redirect('/pedidos/recovery')

@bp_pedidos.route('/recovery', methods=['GET'])
def recovery():
    if request.method == 'GET':
        pedidos = Pedido.query.all()
        return render_template('pedidos_recovery.html', pedidos=pedidos)
    
@bp_pedidos.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    pedido = Pedido.query.get(id)
    
    if request.method == 'GET':
        return render_template('pedidos_update.html', pedido=pedido)
    
    if request.method == 'POST':
        usuario_id = request.form.get('usuario_id')
        pizza_id = request.form.get('pizza_id')
        pedido.usuario_id = usuario_id
        pedido.pizza_id = pizza_id
        
        db.session.add(pedido)
        db.session.commit()
        
        return redirect('/pedidos/recovery')

@bp_pedidos.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    pedido = Pedido.query.get(id)
    
    if request.method == 'GET':
        return render_template('pedidos_delete.html', pedido=pedido)
    
    if request.method == 'POST':
        db.session.delete(pedido)
        db.session.commit()
        
        return redirect('/pedidos/recovery')