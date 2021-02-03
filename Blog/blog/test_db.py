from blog.manage import Book, Author, app, db
from blog.config.setting import MYSQL_PASSWD, MYSQL_DB, MYSQL_HOST, MYSQL_PORT, MYSQL_USER
import unittest
import time


class TestManageDB(unittest.TestCase):

    """定义测试案例"""
    def setUp(self) -> None:
        """在执行具体测试方法前，先被调用"""

        # 激活测试标志
        app.config['TESTING'] = True

        # 设置用来测试的数据库，避免使用正式数据库实例[覆盖原来项目中的数据库配置]
        user = 'root'
        password = '123456'
        # 设置数据库，测试之前需要创建好 create database testdb charset=utf8;
        database = 'flask_ex'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)

        self.app = app

        # 创建数据库的所有模型表：Author、Book模型表
        db.create_all()

    def tearDown(self) -> None:
        # 测试结束时删除数据库
        db.session.remove()
        db.drop_all()

    def test_append_data(self):
        au = Author(name='Alex')
        bk = Book(info='Python_book')
        db.session.add_all([au, bk])
        db.session.commit()
        author = Author.query.first()
        book = Book.query.first()
        self.assertIsNotNone(author)
        self.assertIsNotNone(book)


if __name__ == '__main__':
    unittest.main()



















