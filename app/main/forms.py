from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class NameForm(FlaskForm):
    name = StringField('What is your company\'s name?', validators=[
        DataRequired()])
    submit = SubmitField('Submit')


class GenerateKeyFrom(FlaskForm):
    hasp_id = StringField('Hasp ID', validators=[
        DataRequired(), Length(1, 64), Regexp(
            '^[0-9]*$', 0, 'must have only numbers')])
    musk = StringField('Musk', validators=[
        DataRequired(), Length(1, 64), Regexp(
            '^[0-9]*$', 0, 'must have only numbers')])
    password = StringField('Password', validators=[
        DataRequired(), Length(1, 64), Regexp(
            '^[0-9]*$', 0, 'must have only numbers')])
    clays = StringField('Days', validators=[
        DataRequired(), Length(1, 64), Regexp(
            '^[0-9]*$', 0, 'must have only numbers')])
    submit = SubmitField('Generate')