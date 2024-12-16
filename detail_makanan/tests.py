from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Food
from .models import FoodReviews
import json

class FoodDetailsViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

        self.food = Food.objects.create(
            user=self.user,
            name='Sate Ayam',
            price=25000,
            restaurant='Warung Sate',
            address='Jalan Kenangan',
            contact='08123456789',
            open_time='10:00 - 22:00',
            description='Sate ayam lezat',
            image='sate.jpg'
        )

        self.food_review = FoodReviews.objects.create(
            user=self.user,
            food=self.food,
            review='Enak sekali!',
            rating=5
        )

    def test_show_food_details_get(self):
        response = self.client.get(reverse('dashboard:show_food_details', args=[self.food.id]), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertIn('Enak sekali!', data['html'])

    def test_show_food_details_post(self):
        response = self.client.post(reverse('dashboard:show_food_details', args=[self.food.id]), {
            'review': 'Sangat enak!',
            'rating': 5
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertIn('Sangat enak!', data['html'])

    def test_show_food_details_post_invalid(self):
        response = self.client.post(reverse('dashboard:show_food_details', args=[self.food.id]), {
            'review': '',
            'rating': 5
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertFalse(data['success'])

    def test_delete_food_details_success(self):
        response = self.client.post(reverse('dashboard:delete_food_details', args=[self.food_review.id]))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Review deleted successfully')
        self.assertFalse(FoodReviews.objects.filter(id=self.food_review.id).exists())

    def test_delete_food_details_not_found(self):
        fake_id = 999
        response = self.client.post(reverse('dashboard:delete_food_details', args=[fake_id]))
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Review not found or not authorized.')

    def test_delete_food_details_invalid_method(self):
        response = self.client.get(reverse('dashboard:delete_food_details', args=[self.food_review.id]))
        self.assertEqual(response.status_code, 405)
        data = json.loads(response.content)
        self.assertEqual(data['error'], 'Invalid request method.')
