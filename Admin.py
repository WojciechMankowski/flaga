from flask import Blueprint, render_template, request
from Forms.Login import Login
from app import User

admin = Blueprint("admin", __name__)

@admin.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        print(form.data)
        passwordindb = User.query.filter_by(name=form.data['name']).frist()
        print(passwordindb)
        return render_template("admin/login.html", form=form)
    return render_template("admin/login.html", form=form)

@admin.route("/panel", methods=["GET", "POST"])
def panel_admin():
    return render_template("admin/panel.html")