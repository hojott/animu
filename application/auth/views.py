from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm, EditForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                                error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if (User.query.filter_by(username=form.username.data).first() != None):
        return render_template("auth/register.html", form=form, error="The username you entered is already taken")

    if (form.password.data != form.pw_check.data):
        return render_template("auth/register.html", form=form, error="Passwords didn't match")

    new_user = User(form.name.data, form.username.data, form.password.data)

    db.session().add(new_user)
    db.session().commit()

    login_user(new_user)
    return redirect(url_for("index"))

@app.route("/auth/edit.html", methods = ["GET", "POST"])
@login_required
def auth_edit():
    if request.method == "GET":
        return render_template("auth/edit.html", form=EditForm(obj=current_user))

    form = EditForm(request.form)

    if (form.password_new.data != ""):
        if (form.password_old.data != current_user.password):
            return render_template("auth/edit.html", form=form, error="Wrong password!")

        if (form.password_new.data != form.password_check.data):
            return render_template("auth/edit.html", form=form, error="New passwords didn't match")

        current_user.password = form.password_new.data

    current_user.name = form.name.data
    current_user.username = form.username.data
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/auth/delete", methods=["POST"])
@login_required
def auth_delete():
    # TODO
    return redirect(url_for("index"))