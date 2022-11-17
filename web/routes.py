from web import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    data = {
        'name': 'Timur',
        'age': 34,
        'title': 'Main page'
    }
    html = render_template('shop/index.html', **data)
    return html


@app.route('/login')
def login():
    return render_template('user/login.html', title='Login')
