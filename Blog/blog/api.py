from flask import Flask, jsonify, request
import re
from blog.mysqldb import MysqlDb
from blog.config.setting import MYSQL_DB, MYSQL_PASSWD, MYSQL_HOST, MYSQL_PORT, MYSQL_USER

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

db = MysqlDb(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB)


@app.route('/users', methods=['GET'])
def get_all_users():
    """查询所有用户信息"""
    sql = 'SELECT * FROM user'
    data = db.select_db(sql)
    print('获取所有用户信息 == >> {}'.format(data))
    return jsonify({'code': 0, 'data': data, 'msg': '查询成功'})


@app.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    sql = "SELECT * FROM user WHERE username='{}'".format(username)
    data = db.select_db(sql)
    print('获取 {} 用户信息 == >> {}'.format(username, data))
    if data:
        return jsonify({'code': 0, 'data': data, 'msg': '查询成功'})
    return jsonify({'coed': 1004, 'msg': '查不到相关用户的信息'})


@app.route('/register', methods=['POST'])
def user_register():
    """用户注册"""
    username = request.json.get('username').strip()
    password = request.json.get('password').strip()
    sex = str(request.json.get('sex')).strip()
    telephone = request.json.get('telephone').strip()
    address = request.json.get('address').strip()
    if username and password and telephone:
        sql1 = "SELECT username FROM user WHERE username='{}'".format(username)
        res1 = db.select_db(sql1)
        print('查询到用户名 == >> {}'.format(res1))
        sql2 = "SELECT telephone FROM user WHERE telephone='{}'".format(telephone)
        res2 = db.select_db(sql2)
        print('查询到手机号 == >> {}'.format(res2))
        if res1:
            return jsonify({'code': 2002, 'msg': '用户名已存在，注册失败！！！'})
        elif not (sex == "0" or sex == "1"):
            return jsonify({"code": 2003, "msg": "输入的性别只能是 0(男) 或 1(女)！！！"})
        elif not (len(telephone) == 11 and re.match(r"^1[3-9]\d{9}$", telephone)):
            return jsonify({'code': 2004, 'msg': '手机号格式不正确！！！'})
        elif res2:
            return jsonify({'code': 2005, 'msg': '手机号已经注册！！！'})
        else:
            sql3 = "INSERT INTO user(username, password, role, sex, telephone, address) " \
                   "VALUE ('{}', '{}', '1', '{}', '{}'. '{}')".format(username, password, sex, telephone, address)
            db.execute_db(sql3)
            print('新增用户信息 == >> {}'.format(sql3))
            return jsonify({'code': 0, 'msg': '恭喜，注册成功！'})
    else:
        return jsonify({'code': 2001, 'msg': '用户名/密码/手机号不能为空，请检查！！！'})


@app.route('/login', methods=['POST'])
def user_login():
    """"用户登录"""
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    print('=================>>>>>', password)
    if username and password:
        sql1 = "SELECT username FROM user WHERE username='{}'".format(username)
        res1 = db.select_db(sql1)
        print('查询到用户名 ==>> {}'.format(res1))
        if not res1:
            return jsonify({'code': 1003, 'msg': '用户名不存在！！！'})
        sql3 = "SELECT password FROM user WHERE username='{}'".format(username)
        res3 = db.select_db(sql3)
        print('查询到用户密码 == >> {}'.format(res3))
        if password != res3[0].get('password'):
            return jsonify({'code': 1004, 'msg': '密码错误！！！'})
        sql2 = "SELECT * FROM user WHERE username='{}'".format(username)
        res2 = db.select_db(sql2)
        print('获取 {} 用户信息 == >> {}'.format(username, res2))
        if res2:
            return jsonify({'code': 0, 'msg': '恭喜，登录成功！'})
    else:
        return jsonify({'code': 1001, 'msg': '用户名或密码不能为空！！！'})



