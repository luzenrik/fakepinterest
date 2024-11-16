from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desabilita o rastreamento de modificações do banco de dados para melhorar o desempenho

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"  # Define a URI de conexão com o banco de dados SQLite

app.config["SECRET_KEY"] = "c4cc65b56cef9900d5557777b2a01e8f"  # Define uma chave secreta para o gerenciamento de sessões e segurança de cookies

database = SQLAlchemy(app)  # Cria a instância do banco de dados
bcrypt = Bcrypt(app)         # Cria a instância do gerenciador de hash de senhas
login_manager = LoginManager(app)  # Cria a instância do gerenciador de login

# Define a view de login que será usada caso o usuário tente acessar uma página protegida
login_manager.login_view = "homepage"  # Página de login (homepage) se o usuário não estiver autenticado

# Função que carrega o usuário baseado no seu ID (requerido pelo Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    # Importa o modelo Usuario do módulo fakepinterest.models (evitar importação circular)
    from fakepinterest.models import Usuario
    # Retorna o usuário correspondente ao ID
    return Usuario.query.get(int(user_id)) 

# Importa as rotas do módulo 'routes' onde são definidas as views da aplicação
from fakepinterest import routes