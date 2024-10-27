from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Food, Bookmark
import json
import uuid

class MainAppTests(TestCase):
    def setUp(self):
        # Set up user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

        # Set up sample Food object
        self.food = Food.objects.create(
            name='Nasi Goreng',
            price=20000,
            restaurant='Warung Makan',
            address='Jalan Merdeka',
            contact='08123456789',
            open_time='08:00 - 22:00',
            description='Nasi goreng lezat',
            user=self.user
        )

    def test_main_url_is_exist(self):
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        response = self.client.get(reverse('main:register'))
        self.assertEqual(response.status_code, 200)

    def test_login_logout(self):
        login_response = self.client.post(reverse('main:login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(login_response.status_code, 302)  # Redirect setelah login berhasil

        # Testing logout
        response = self.client.get(reverse('main:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect setelah logout berhasil

    def test_show_bookmarks(self):
        Bookmark.objects.create(user=self.user, food=self.food)
        response = self.client.get(reverse('main:show_bookmarks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nasi Goreng')

   

    def test_show_json(self):
        response = self.client.get(reverse('main:show_json'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data[0]['fields']['name'], 'Nasi Goreng')

    def test_bookmark_food(self):
        response = self.client.post(reverse('main:bookmark_food', args=[self.food.id]))
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertTrue(data['is_bookmarked'])

    def test_remove_bookmark(self):
        Bookmark.objects.create(user=self.user, food=self.food)
        response = self.client.post(reverse('main:bookmark_food', args=[self.food.id]))
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertFalse(data['is_bookmarked'])
        
    def test_bookmark_list(self):
        Bookmark.objects.create(user=self.user, food=self.food)
        response = self.client.get(reverse('main:bookmark', args=[self.food.id]))
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertTrue(data['is_bookmarked'])

