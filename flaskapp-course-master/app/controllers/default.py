from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

# Retorna o Hello, World! típico
# Duas rotas diferentes para mesma classe
@app.route("/index/<user>", methods=['GET'])
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user) # Renderiza o HTML


# Página de Login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid Login.")    
    return render_template('login.html', form=form)

# Página de Logout
@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))

# Retorna um valor default
@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, Usuário!"

# Força retorno de um inteiro
@app.route("/print/<int:id>")
def printar(id):
    print(type(id))
    return ""

# Brinca com o Banco de Dados
@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):
    i = User("felipebraga", "senha_dificil", "Felipe", 
            "felipe@felipe.com")
    # Adiciona a fila para subir para o db
    # db.session.add(i)
    # Adiciona ao banco
    # db.session.commit()
    # buscar as informaçoes no db
    # r = User.query.filter_by(username="felipebraga").first()
    # print(r.username, r.name)
    return 'OK'
