from flask import Flask
from flask import render_template

'''配置数据库'''
app = Flask(__name__)
app.config['SECRET_KEY'] ='hard to guess'


@app.route('/')
@app.route('/index')
def index():
    user = {'nikename': 'Jane'}
    posts = [
        {
            'author': {'nickname': 'Susan'}, 
            'body': 'Beautiful day in Portland!'},
        {
            'author': {'nickname': 'Miguel'}, 
            'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    pass


@app.route('/register')
def register():
    pass


@app.route('/about')
def about():
    return render_template('about.html', title='About')



