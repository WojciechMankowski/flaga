from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    name = StringField("Nazwa: ", validators=[DataRequired()])
    password = PasswordField("Hasło: ", validators=[DataRequired()])
