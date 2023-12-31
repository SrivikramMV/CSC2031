from flask import Blueprint, render_template

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/')
def register():
    return render_template('users/register.html')

@users_blueprint.route('/')
def login():
    return render_template('users/login.html')

@users_blueprint.route('/')
def account():
    return render_template('users/account.html')