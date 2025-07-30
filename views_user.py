from flask import render_template, request, redirect, session, flash, url_for
from flask_bcrypt import check_password_hash
from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario


@app.route("/login")
def login():
    proxima = request.args.get("proxima")

    form = FormularioUsuario()

    return render_template("login.html", proxima=proxima, form=form)


@app.route("/autenticar", methods=["POST"])
def autenticar():

    form = FormularioUsuario(request.form)

    if form.validate_on_submit():
        usuario = Usuarios.query.filter_by(nickname=form.apelido.data).first()
        senha = check_password_hash(usuario.senha, form.senha.data)

        if usuario and senha:
            session["usuario_logado"] = usuario.nickname
            flash(usuario.nickname + " logado com sucesso!")
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)

    flash("Usuario não logado!")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Usuario deslogado com sucesso!")
    return redirect(url_for("index"))
