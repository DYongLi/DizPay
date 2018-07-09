from flask import render_template, Blueprint, jsonify
from app.views import Api

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/login')
def login():
    return render_template('login.html')


@home.route('/wallet')
def wallet():
    return render_template('wallet.html')


@home.route("/payment")
def payment():
    return render_template('accept_payment.html')