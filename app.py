import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy import ForeignKey
from werkzeug.utils import secure_filename
from Forms.AddPost import add_new_post
from Forms.Login import Login
from Forms.ProjectForm import Project
from ListCategory import list_category, category_images
from Forms.Contact import Contact

# server name = wojtek92!
# hasło Aparat22
# name db blog


app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
app.config['SECRET_KEY'] = 'my_screat_key'
app.config['UPLOAD_FOLDER'] = "./static/IMAG"


ALLOWED_EXTENSIONS = ["jpg", "png"]
db = SQLAlchemy(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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
        """False, as anonymous users aren't.db supported."""
        return False


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    slug = db.Column(db.String(250))
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(250))
    Photo = db.Column(db.String(250))
    content = db.Column(db.Text)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    comment = db.Column(db.Text)
    id_posta = db.Column(db.Integer, ForeignKey("post.id"))


class PortfolioDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    programmingLanguage = db.Column(db.String(250))
    description = db.Column(db.String(250))
    url = db.Column(db.String(250))


@app.route('/')
def index():
    list_poty = Post.query.all()
    index = len(list_poty) - 1
    post = []
    while index != -1:
        post.append(list_poty[index])
        index -= 1
    lenpost = len(post)
    true_or_false = lenpost == 0
    return render_template("index.html", list_poty=post, true_or_false=true_or_false)


@app.route("/categories")
def category():
    return render_template("categories.html", category=list_category, img=category_images)


@app.route("/category/<category>")
def Category(category: str):
    list_posty = Post.query.filter_by(category=category)
    return render_template("category.html", category=category, list_posty=list_posty)


@app.route("/contact" , methods=["GET", "POST"])
def contact():
    form = Contact()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.data)
        return render_template("contact.html", form=form)
    return render_template("contact.html", form=form)


@app.route("/<title>")
def post(title: str):
    post = Post.query.filter_by(slug=title).first()
    return render_template("post.html", post=post)


@app.route("/portfolio")
def portfolio():
    listportfolio = PortfolioDB.query.all()
    return render_template("portfolio.html", listportfolio=listportfolio)
# podziękowania zapisania na newsletter
# podziękowania za wysłanie wiadomości


@app.route("/admin/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        user_db = User.query.filter_by(name=form.data['name']).first()
        if isinstance(user_db, User):
            if user_db.password == form.data["password"]:
                login_user(user_db)
                return redirect(url_for("panel_admin"))
            else:
                return render_template("admin/login.html", form=form, messege="Błędne dane do logowania!!")
        else:
            return render_template("admin/login.html", form=form, messege="Błędne dane do logowania!!")
    return render_template("admin/login.html", form=form)


@app.route("/admin/panel", methods=["GET", "POST"])
def panel_admin():
    if current_user.is_authenticated:
        return render_template("admin/panel.html", user=current_user.is_authenticated)
    else:
        return redirect(url_for("login"))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/admin/new_post", methods=["GET", "POST"])
@login_required
def addpost():
    if current_user.is_authenticated:
        form = add_new_post()
        author = "Wojciech Mankowski"
        data = datetime.now()
        if form.validate_on_submit() or request.method == "POST":
            slug = form.data["title"].replace(" ", "_")
            image = request.files["image"]
            name_file = image.filename
            if name_file == "":
                flash('No selected file')
                return redirect(request.url)
            elif image and allowed_file(name_file):
                filename = secure_filename(name_file)
                patch = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(patch)
            new_post = Post(title=form.data["title"], slug=slug, author=author,
                            date_posted=data, category=form.data["category"],
                            content=form.content.data, Photo=f"IMAG/{name_file}")
            db.session.add(new_post)
            db.session.commit()
        return render_template("admin/newpost.html", user=current_user.is_authenticated, form=form)
    else:
        return redirect(url_for("login"))


@app.route("/admin/newproject", methods=["GET", "POST"])
@login_required
def addproject():
    if current_user.is_authenticated:
        form = Project()
        print(form.validate_on_submit())
        if form.validate_on_submit():
            data = form.data
            print(data)
            programmingLanguage = ""
            for item in data["programmingLanguage"]:
                if data["programmingLanguage"][-1] == item:
                    programmingLanguage += item
                else:
                    programmingLanguage += item + ", "
            project = PortfolioDB(name=data["name"], programmingLanguage=programmingLanguage,
                                  description=data["description"], url=data["url"])
            db.session.add(project)
            db.session.commit()
            return redirect(url_for("portfolio"))

        return render_template("admin/newproject.html", user=current_user.is_authenticated, form=form)
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


if __name__ == "__main__":
    app.run()
    # set FLASK_ENV=development
