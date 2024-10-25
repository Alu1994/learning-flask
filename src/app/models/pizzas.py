from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from .tables import Pizza
from app import db

bp_pizzas = Blueprint("pizzas", __name__, template_folder="templates", static_folder="static")

@bp_pizzas.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('pizzas_create.html')
    
    if request.method == 'POST':
        sabor = request.form.get('sabor')
        imagem = request.form.get('imagem')
        ingredientes = request.form.get('ingredientes')
        preco = request.form.get('preco')
        
        pizza = Pizza(sabor, imagem, ingredientes, preco)
        db.session.add(pizza)
        db.session.commit()
        
        return redirect('/pizzas/recovery')

@bp_pizzas.route('/recovery', methods=['GET'])
def recovery():
    if request.method == 'GET':
        pizzas = Pizza.query.all()
        return render_template('pizzas_recovery.html', pizzas=pizzas)
    
@bp_pizzas.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    pizza = Pizza.query.get(id)
    
    if request.method == 'GET':
        return render_template('pizzas_update.html', pizza=pizza)
    
    if request.method == 'POST':        
        sabor = request.form.get('sabor')
        imagem = request.form.get('imagem')
        ingredientes = request.form.get('ingredientes')
        preco = request.form.get('preco')
        
        pizza.sabor = sabor
        pizza.imagem = imagem
        pizza.ingredientes = ingredientes
        pizza.preco = preco
        
        db.session.add(pizza)
        db.session.commit()
        
        return redirect('/pizzas/recovery')

@bp_pizzas.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    pizza = Pizza.query.get(id)
    
    if request.method == 'GET':
        return render_template('pizzas_delete.html', pizza=pizza)
    
    if request.method == 'POST':
        db.session.delete(pizza)
        db.session.commit()
        
        return redirect('/pizzas/recovery')