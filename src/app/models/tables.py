from database import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
        
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
            
    def __repr__(self):
        return f'Usuario: {self.nome}'
    
class Pizza(db.Model):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(100))
    imagem = db.Column(db.String(100))
    ingredientes = db.Column(db.String(100))
    preco = db.Column(db.Float)    
        
    def __init__(self, sabor, imagem, ingredientes, preco):
        self.sabor = sabor
        self.imagem = imagem
        self.ingredientes = ingredientes
        self.preco = preco
    
    def __repr__(self):
        return f'Pizza: {self.sabor}'

class Pedido(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    data = db.Column(db.Date)
    
    usuario = db.relationship('Usuario', foreign_keys=usuario_id)
    pizza = db.relationship('Pizza', foreign_keys=pizza_id)
    
    def __init__(self, usuario_id, pizza_id, data):
        self.usuario_id = usuario_id
        self.pizza_id = pizza_id
        self.data = data
    
    def __repr__(self):
        return f'Pedido: {self.id} {self.usuario.nome} {self.pizza.sabor}'