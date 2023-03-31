from django.test import TestCase
from django.contrib.auth.models import User
from user.models import UserProfile
from news.models import News, Likes, Comments
import json
from django.urls import reverse

class UserTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser', password='Host86rc')
        profile = UserProfile.objects.get(user=user)
        profile = UserProfile.objects.update(phone='89288131995', firstname='Родионов', lastname='Ярослав', status='Счатстье внутри тебя!')
        user = self.client.login(username='testuser', password='Host86rc')

    # тест на запрос страницы профиля
    def test_page_profile(self):
        resp = self.client.get('/user/testuser')
        self.assertEqual(resp.status_code, 200)
    
    # тест на корректность используемого шаблона
    def test_page_profile_temp(self):
        resp = self.client.get('/user/testuser')
        self.assertTemplateUsed(resp, 'user/profile.html')

    # тест на загрузку контекста в шаблон
    def test_page_profile_context(self):
        resp = self.client.get('/user/testuser')
        self.assertTrue('form' in resp.context)
        self.assertTrue('formprofile' in resp.context)
        self.assertTrue('formadd' in resp.context)
        self.assertTrue('comformadd' in resp.context)
        self.assertTrue('comments' in resp.context)
        self.assertTrue('likes' in resp.context)
        self.assertTrue('profile' in resp.context)
        self.assertTrue('mynews' in resp.context)
        self.assertTrue('friends' in resp.context)
        self.assertTrue('friendsall' in resp.context)
    
    # тест на добавление, лайк и удаление поста в профиле
    def test_page_profile_add_news(self):
        user = User.objects.get(username='testuser')
        url = reverse('profile', kwargs={'username': user.username})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # Добавление поста #####################
        form_data = {
            'text': 'Test news text',
            'images': '',
            'files': '',
            'athor': user.pk
        }
        resp = self.client.post(url, data=form_data)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('profile', kwargs={'username': user.username}))
        newsadd = News.objects.get(text='Test news text')
        self.assertEqual(newsadd.pk, 1)
        
        # Комментирование поста #####################
        form_data = {
            'text': 'Test news text',
            'new': 1,
            'user': user.pk,
        }
        resp = self.client.post('/addcom/', form_data)
        comment = Comments.objects.filter(user=1).filter(new=1).filter(text='Test news text')
        self.assertEqual(comment.first().text, 'Test news text')
        
        # Лайк поста #####################
        resp = self.client.get('/like/', {'post_id': 1})
        like = Likes.objects.filter(user=1).filter(new=1)
        self.assertEqual(str(like.first()), 'testuser лайкнул Пост id-1 от testuser')
        # Удаление поста #####################
        resp = self.client.get('/user/del_post/', {'post_id': 1})
        try:
            newsadd = News.objects.get(text='Test news text')
        except Exception:
            newsadd = '0'
        self.assertEqual(newsadd, '0')

    # тест на запрос страницы чат
    def test_page_chat(self):
        resp = self.client.get('/chat/testuser')
        self.assertEqual(resp.status_code, 200)

    # тест на запрос страницы мои друзья
    def test_page_friends(self):
        resp = self.client.get('/friends/')
        self.assertEqual(resp.status_code, 200)

    # тест на запрос страницы новости
    def test_page_news(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    # тест на запрос страницы избранное
    def test_page_favorites(self):
        resp = self.client.get('/favorites/')
        self.assertEqual(resp.status_code, 200)

    # тест на запрос страницы api
    def test_page_api(self):
        resp = self.client.get('/api')
        self.assertEqual(resp.status_code, 200)
    