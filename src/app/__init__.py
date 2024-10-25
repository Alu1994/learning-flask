from flask import Flask
from database import db
from flask_migrate import Migrate
from .models.usuarios import bp_usuarios
from .models.pizzas import bp_pizzas
from .models.pedidos import bp_pedidos

app = Flask(__name__)

conexao = 'sqlite:///mydb.sqlite'
app.config['SECRET_KEY'] = 'minha-palavra-secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_pizzas, url_prefix='/pizzas')
app.register_blueprint(bp_pedidos, url_prefix='/pedidos')

from app import routes