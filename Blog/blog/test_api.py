import unittest
import json
from blog.api import user_login, user_register, get_all_users, get_user
from blog.api import app


class APITestCase(unittest.TestCase):
    """定义测试案例"""

    def setUp(self) -> None:
        """在执行具体测试方案之前，先被调用"""
        self.app = app
        # 激活测试标志
        app.config.update(
            TESTING=True
        )
        # app.config['TESTING'] = True
        # 在这里使用flask提供的测试客户端进行测试
        self.client = app.test_client()

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_get_all_user(self):
        response = self.client.get('/users')
        res = response.get_data(as_text=True)
        self.assertNotEqual(0, len(json.loads(res).get('data')))

    def test_get_user(self):
        response = self.client.get('/users/Michael')
        res = response.get_data(as_text=True)
        result = json.loads(res)
        self.assertEqual('Michael', result.get('data')[0].get('username'))

    def test_login_username_or_password_is_null(self):
        """测试模拟场景，用户名为空"""
        response = self.client.post("/login", data={'username': '', 'password': '123456'})
        res = response.data
        result = json.loads(res)
        self.assertEqual(1001, result.get('code'))

        response = self.client.post('/login', data={'username': 'Joe', 'password': ''})
        # response.data 是响应体数据
        resp_json = response.data
        # 按照json解析
        resp_dict = json.loads(resp_json)
        self.assertEqual(1001, resp_dict.get('code'))

    def test_login_username_is_wrong(self):
        """测试模拟场景，用户名不存在"""
        response = self.client.post('/login', data={'username': 'Jan', 'password': '123456'})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertEqual(1003, resp_dict.get('code'))

    def test_login_password_is_wrong(self):
        """测试密码错误"""
        response = self.client.post('/login', data={'username': 'Joe', 'password': '1123456'})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertEqual(1004, resp_dict.get('code'))

    def test_login_success(self):
        """测试登录成功"""
        response = self.client.post('/login', data={'username': 'Joe', 'password': '123456'})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertEqual(0, resp_dict.get('code'))
        self.assertEqual('恭喜，登录成功！', resp_dict.get('msg'))


