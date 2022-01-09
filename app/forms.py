from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField

class InputForm(FlaskForm):
    message = TextAreaField("Message")
    submit = SubmitField("Send")
    file = FileField()
