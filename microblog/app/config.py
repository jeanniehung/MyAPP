import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # 创建表单
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # 数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

