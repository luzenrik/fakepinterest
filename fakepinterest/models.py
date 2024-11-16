# Modelagem do bando de dados

from datetime import datetime
from fakepinterest import database

class Usuario(database.Model):  # Esta classe herda de database.Model, indicando que é um modelo do SQLAlchemy
    id = database.Column(database.Integer, primary_key=True)  # Campo ID, preenchido automaticamente por ser a chave primária
    username = database.Column(database.String, nullable=False)  # Nome de usuário, obrigatório
    email = database.Column(database.String, nullable=False, unique=True)  # Email, obrigatório e único
    senha = database.Column(database.String, nullable=False)  # Senha, obrigatória
    # Define a relação com a tabela "Foto", onde "usuario" é o nome da referência reversa
    fotos = database.relationship("Foto", backref="usuario", lazy=True)

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)  # Campo ID, chave primária
    # Armazena o caminho da imagem; por padrão, é 'default.png'
    imagem = database.Column(database.String, default='default.png')
    # Data de criação, obrigatória, com valor padrão sendo o horário atual
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    # ID do usuário a quem a foto pertence, chave estrangeira referenciando "usuario.id"
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)