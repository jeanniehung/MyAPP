from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Jane Dav',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'April 20, 2020'
    }
]

@app.route("/")
@app.route('/index')
def index():
    # user = {'nickname': 'Jane'}
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)
