from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def inder():
    user = {'username':'Jack'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'This is so scuffed!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Seriously needs patch!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)