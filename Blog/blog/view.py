from flask import Flask, jsonify
from flask import render_template, request
import re
import pymysql
from blog.config.setting import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, SERVER_PORT
from blog.mysqldb import MysqlDb

'''配置数据库'''
app = Flask(__name__)
app.config['SECRET_KEY'] ='hard to guess'


# class MysqlDb(object):
#
#     def __init__(self, host, port, user, passwd, db):
#         # 建立数据库连接
#         self.conn = pymysql.connect(
#             host=host,
#             port=port,
#             user=user,
#             passwd=passwd,
#             db=db
#         )
#         # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
#         self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
#
#     def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
#         # 关闭游标
#         self.cur.close()
#         # 关闭数据库连接
#         self.conn.close()
#
#     def select_db(self, sql):
#         """查询"""
#         # 检查连接是否断开，如果断开就进行重连
#         self.conn.ping(reconnect=True)
#         # 使用 execute() 执行sql
#         self.cur.execute(sql)
#         # 使用 fetchall() 获取查询结果
#         data = self.cur.fetchall()
#         return data
#
#     def execute_db(self, sql):
#         """更新/新增/删除"""
#         try:
#             # 检查连接是否断开，如果断开就进行重连
#             self.conn.ping(reconnect=True)
#             # 使用 execute() 执行sql
#             self.cur.execute(sql)
#             # 提交事务
#             self.conn.commit()
#         except Exception as e:
#             print("操作出现错误：{}".format(e))
#             # 回滚所有更改
#             self.conn.rollback()


# db = MysqlDb(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB)
#
#
# @app.route("/users", methods=["GET"])
# def get_all_users():
#     """获取所有用户信息"""
#     sql = "SELECT * FROM user"
#     data = db.select_db(sql)
#     print("获取所有用户信息 == >> {}".format(data))
#     return jsonify({"code": "0", "data": data, "msg": "查询成功"})
#
#
# @app.route("/users/<string:username>", methods=["GET"])
# def get_user(username):
#     """获取某个用户信息"""
#     sql = "SELECT * FROM user WHERE username = '{}'".format(username)
#     data = db.select_db(sql)
#     print("获取 {} 用户信息 == >> {}".format(username, data))
#     if data:
#         return jsonify({"code": "0", "data": data, "msg": "查询成功"})
#     return jsonify({"code": "1004", "msg": "查不到相关用户的信息"})
#
#
# @app.route("/register", methods=['POST'])
# def user_register():
#     """用户注册"""
#     username = request.json.get("username").strip()  # 用户名
#     password = request.json.get("password").strip()  # 密码
#     sex = str(request.json.get("sex", "0")).strip()  # 性别，默认为0(男性)
#     telephone = request.json.get("telephone", "").strip()  # 手机号，默认为空串
#     address = request.json.get("address", "").strip()  # 地址，默认为空串
#     if username and password and telephone:
#         sql1 = "SELECT username FROM user WHERE username = '{}'".format(username)
#         res1 = db.select_db(sql1)
#         print("查询到用户名 ==>> {}".format(res1))
#         sql2 = "SELECT telephone FROM user WHERE telephone = '{}'".format(telephone)
#         res2 = db.select_db(sql2)
#         print("查询到手机号 ==>> {}".format(res2))
#         if res1:
#             return jsonify({"code": 2002, "msg": "用户名已存在，注册失败！！！"})
#         elif not (sex == "0" or sex == "1"):
#             return jsonify({"code": 2003, "msg": "输入的性别只能是 0(男) 或 1(女)！！！"})
#         elif not (len(telephone) == 11 and re.match("^1[3,5,7,8]\d{9}$", telephone)):
#             return jsonify({"code": 2004, "msg": "手机号格式不正确！！！"})
#         elif res2:
#             return jsonify({"code": 2005, "msg": "手机号已被注册！！！"})
#         else:
#             sql3 = "INSERT INTO user(username, password, role, sex, telephone, address) " \
#                   "VALUES('{}', '{}', '1', '{}', '{}', '{}')".format(username, password, sex, telephone, address)
#             db.execute_db(sql3)
#             print("新增用户信息 ==>> {}".format(sql3))
#             return jsonify({"code": 0, "msg": "恭喜，注册成功！"})
#     else:
#         return jsonify({"code": 2001, "msg": "用户名/密码/手机号不能为空，请检查！！！"})
#
#
# @app.route("/login", methods=['POST'])
# def user_login():
#     """用户登录"""
#     username = request.values.get("username").strip()
#     password = request.values.get("password").strip()
#     if username and password:
#         sql1 = "SELECT username FROM user WHERE username = '{}'".format(username)
#         res1 = db.select_db(sql1)
#         print("查询到用户名 ==>> {}".format(res1))
#         if not res1:
#             return jsonify({"code": 1003, "msg": "用户名不存在！！！"})
#         sql2 = "SELECT * FROM user WHERE username = '{}' and password = '{}'".format(username, password)
#         res2 = db.select_db(sql2)
#         print("获取 {} 用户信息 == >> {}".format(username, res2))
#         if res2:
#             return jsonify({"code": 0, "msg": "恭喜，登录成功！"})
#         return jsonify({"code": 1002, "msg": "用户名或密码错误！！！"})
#     else:
#         return jsonify({"code": 1001, "msg": "用户名或密码不能为空！！！"})


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



