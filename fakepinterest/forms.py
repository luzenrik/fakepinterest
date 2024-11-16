# Os formulários
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField  

from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError  


# Define a classe de formulário para login do usuário.
class FormLogin(FlaskForm):  
    email = StringField("E-mail", validators=[DataRequired(), Email()])  
    senha = PasswordField("Senha", validators=[DataRequired()]) 
    botao_confirmacao = SubmitField("Fazer Login")  

# Define a classe de formulário para criação de nova conta.
class FormCriarConta(FlaskForm):  
    email = StringField("E-mail", validators=[DataRequired(), Email()])  
    usarname = StringField("Nome de usuário", validators=[DataRequired()])  
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)]) 
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")]) 
    botao_confirmacao = SubmitField("Criar Conta") 

    # Método para validar se o email já existe no banco de dados.
    def validade_email(self, email):  
         from fakepinterest import Usuario
         usuario = Usuario.query.filter_by(email=email.data).first()  
         if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")