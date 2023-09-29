import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo


def character_check(form, field):
    excluded_chars = "<&%"

    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")


def validate_password(form, field):
    p = re.compile(r'(?=.*\d)(?=.*[a-z])')
    if not p.match(field.data):
        raise ValidationError('Password must contain 1 digit and one lowercase letter between a and z')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Email(), character_check])
    password = PasswordField('Password', validators=[DataRequired(), character_check, Length(min=8, max=15),
                                                     validate_password])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8, max=15),
                                                                     EqualTo('password', message='Passwords'
                                                                                                 ' must match')])
    submit = SubmitField()
