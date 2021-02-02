import unittest
import json
from blog.api import user_login, user_register, get_all_users, get_user
from blog.api import app


class APITestCase(unittest.TestCase):

    def setUp(self) -> None:
        app.config.update(
            TESTING=True
        )
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
        response = self.client.post("/login", data={'username': '', 'password': '123456'})
        res = response.data
        result = json.loads(res)
        self.assertEqual(1001, result.get('code'))


