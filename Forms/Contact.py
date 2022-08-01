from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, Email
from ListCategory import list_category


class Contact(FlaskForm):
    name = StringField("Twoje imię: ", validators=[
                       DataRequired(), Length(max=250, min=5)])
    email = EmailField("Twój e-mail: ", validators=[DataRequired()])
    title = StringField("Temat: ", validators=[DataRequired()])
    message = TextAreaField("Wiadomość: ", validators=[DataRequired()])
