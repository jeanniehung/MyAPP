from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

class Config(object):
    """设置配置参数"""
    user = 'root'
    password = '123456'
    database = 'mysql_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User',backref='role') # 反推与role关联的多个User模型对象


class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 设置外键


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

if __name__ == '__main__':
    # 删除所有表
    db.drop_all()

    # 创建所有表
    db.create_all()
    app.run(debug=True)

