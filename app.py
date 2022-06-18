from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from Forms.Login import Login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
app.config['SECRET_KEY'] = 'my_screat_key'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    e_mail = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return f"User name: {self.name}"

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html")

@app.route("/category")
def category():
    return render_template("category.html")

@app.route("/contact")

def contact():
    return render_template("contact.html")
# pojedyńczy wpis
# podziękowania zapisania na newsletter
# podziękowania za wysłanie wiadomości



@app.route("/admin/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        print(form.data)
        user_db = User.query.filter_by(name=form.data['name']).first()
        if user_db.password == form.data["password"]:
            login_user(user_db)
            return redirect(url_for("panel_admin"))
        else:
            return render_template("admin/login.html", form=form, messege="Błędne dane do logowania!!")
    return render_template("admin/login.html", form=form)

@app.route("/admin/panel", methods=["GET", "POST"])
def panel_admin():
    if current_user.is_authenticated:
        return render_template("admin/panel.html", login_manager=login_manager, user=current_user.is_authenticated)
    else:
        return redirect(url_for("login"))

@app.route("/admin/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return render_template("admin/logout.html")

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

if __name__=="__main__":

    app.run()
