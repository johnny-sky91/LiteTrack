from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from app import db
from app.auth import bp
from app.models.auth import User
from app.auth.forms import RegistrationForm, LoginForm


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("all_complaints"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have signed up")
        return redirect(url_for("login"))
    return render_template("auth/register.html", title="To_fill?", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("/"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return url_for("/")
    return render_template("auth/login.html", title="To_fill?", form=form)
