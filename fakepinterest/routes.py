from flask import render_template, url_for  # Importa a função render_template para renderizar páginas HTML e url_for para gerar URLs dinâmicas.
from fakepinterest import app  # Importa a instância do Flask criada em fakepinterest para definir rotas e configurações da aplicação.
from flask_login import login_required  # Importa o decorador login_required para restringir o acesso de rotas a usuários autenticados.
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET","POST"]) 
def homepage():  
    form_login = FormLogin()
    return render_template("homepage.html", form= form_login ) 

@app.route("/criarconta", methods=["GET","POST"])  
def criarconta(): 
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<usuario>") 
@login_required
def perfil(usuario):
    return render_template("perfil.html", nome=usuario)