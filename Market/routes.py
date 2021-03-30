from flask import render_template

from Market import app
# from Market.forms import RegisterForm
from Market.models import Item


@app.route('/')
@app.route('/home')
def home_page_view():
    return render_template('home.html')


@app.route('/market')
def market_page_view():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page_view():
    form = RegisterForm()
    return render_template('register.html', form=form)
