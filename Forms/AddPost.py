from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length
from ListCategory import list_category

class add_new_post(FlaskForm):
    title = StringField("Tytuł posta: ", validators=[DataRequired(), Length(max=250, min=5)])
    category = SelectField("Kategoria: ", choices=list_category,  validators=[DataRequired()])
    content = TextAreaField("Treść posta: ", validators=[DataRequired(), Length(min=100)])
    image = FileField(validators=[FileRequired()])