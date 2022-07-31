from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, URLField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length

programmingLanguages = [
    "HTML", "CSS", "JavaScript", "Python", "React", "TypeScript"
]


class Project(FlaskForm):
    name = StringField("Nazwa projektu: ", validators=[
                       DataRequired(), Length(max=250, min=5)])
    programmingLanguage = SelectMultipleField(
        "Wykorzystywane języki i technologie: ", choices=programmingLanguages)
    description = TextAreaField("Opis projeku: ", validators=[DataRequired()])
    url = URLField("Link do repezytorium")
