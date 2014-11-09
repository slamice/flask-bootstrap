from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    title = 'Home'
    posts = [
        {
            'author': {'nickname': 'john'},
            'body':'Stuff going on'
        },
        {
            'author': {'nickname': 'dude'},
            'body':'Stuff going on'
        }
    ]
    return render_template('index.html', title=title, user=user, posts=posts)
