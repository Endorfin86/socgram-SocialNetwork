from django.test import TestCase
from django.contrib.auth.models import User
import time

class UserTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='Host86rc')

    def tearDown(self):
        pass

    # тест на запрос страницы /user/login
    def test_login(self):
        resp = self.client.get('/user/login')
        self.assertEqual(resp.status_code, 200)

    # тест на запрос авторизации пользователя
    def test_login_auth(self):
        resp = self.client.post('/user/login', {'username':'testuser', 'password':'Host86rc'})
        self.assertEqual(resp.status_code, 302)
        user = User.objects.get(username='testuser')
        self.assertEqual(user.is_authenticated, True)

    # тест на запрос страницы /user/registration и регистрации нового пользователя
    def test_register(self):
        resp = self.client.get('/user/registration')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post('/user/registration', {'username':'testuser2', 'email':'test@user.ru', 'password1':'Host86rc', 'password2':'Host86rc'})
        user = User.objects.get(username='testuser2')
        self.assertEqual(user.username, 'testuser2')
        self.assertEqual(user.email, 'test@user.ru')
