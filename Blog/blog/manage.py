from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from blog.config.setting import MYSQL_PASSWD, MYSQL_DB, MYSQL_USER, MYSQL_PORT, MYSQL_HOST
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
manager = Manager(app)


class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = MYSQL_USER
    password = MYSQL_PASSWD
    database = MYSQL_DB
    port = MYSQL_PORT
    host = MYSQL_HOST
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (user, password, host, port, database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    # app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

    # 设置密钥，用于csrf_token的加解密
    app.config["SECRET_KEY"] = "xhosd6f982yfhowefy29f"


# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

# 第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app, db)

# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db', MigrateCommand)


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), unique=True)
    email = db.Column(db.String(64))
    au_book = db.relationship('Book', backref='author')

    def __str__(self):
        return 'Author:%s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32), unique=True)
    leader = db.Column(db.String(32))
    au_book = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __str__(self):
        return 'Book:%s,%s' % (self.info, self.leader)























