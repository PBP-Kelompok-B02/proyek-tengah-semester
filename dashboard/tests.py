from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Food
import json
import uuid

class DashboardViewsTests(TestCase):
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

    def test_show_profile(self):
        response = self.client.get(reverse('dashboard:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, 'Sate Ayam')

    def test_change_password_success(self):
        response = self.client.post(reverse('dashboard:change_password'), {
            'old_password': 'testpass',
            'new_password': 'newtestpass',
            'confirm_password': 'newtestpass'
        })
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], 'Password changed successfully')

    def test_change_password_failure(self):
        response = self.client.post(reverse('dashboard:change_password'), {
            'old_password': 'wrongpass',
            'new_password': 'newtestpass',
            'confirm_password': 'newtestpass'
        })
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Old password is incorrect')

    def test_get_user_foods(self):
        response = self.client.get(reverse('dashboard:get_user_foods'))
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(len(data['foods']), 1)
        self.assertEqual(data['foods'][0]['name'], 'Sate Ayam')

    def test_add_food_entry_ajax_success(self):
        response = self.client.post(reverse('dashboard:add_food'), {
            'name': 'Nasi Goreng',
            'price': 20000,
            'restaurant': 'Warung Nasi',
            'address': 'Jalan Kenangan',
            'contact': '08123456789',
            'open_time': '08:00 - 20:00',
            'description': 'Nasi goreng enak',
            'image': 'nasigoreng.jpg'
        })
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertTrue(Food.objects.filter(name='Nasi Goreng').exists())

    def test_add_food_entry_ajax_failure(self):
        response = self.client.post(reverse('dashboard:add_food'), {
            'name': '',
            'price': 20000,
            'restaurant': 'Warung Nasi',
            'address': 'Jalan Kenangan',
            'contact': '08123456789',
            'open_time': '08:00 - 20:00',
            'description': 'Nasi goreng enak',
            'image': 'nasigoreng.jpg'
        })
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertFalse(Food.objects.filter(restaurant='Warung Nasi').exists())

    def test_edit_food_ajax_success(self):
        response = self.client.post(reverse('dashboard:edit_food', args=[self.food.id]), {
            'name': 'Sate Kambing',
            'price': 30000,
            'restaurant': 'Warung Sate',
            'address': 'Jalan Kenangan',
            'contact': '08123456789',
            'open_time': '10:00 - 22:00',
            'description': 'Sate kambing lezat',
            'image': 'satekambing.jpg'
        })
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertTrue(Food.objects.filter(name='Sate Kambing').exists())

    def test_edit_food_ajax_failure(self):
        response = self.client.post(reverse('dashboard:edit_food', args=[self.food.id]), {
            'name': '',
            'price': 30000,
            'restaurant': 'Warung Sate',
            'address': 'Jalan Kenangan',
            'contact': '08123456789',
            'open_time': '10:00 - 22:00',
            'description': 'Sate kambing lezat',
            'image': 'satekambing.jpg'
        })
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')

    def test_delete_food_ajax_success(self):
        response = self.client.post(reverse('dashboard:delete_food', args=[self.food.id]))
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertFalse(Food.objects.filter(id=self.food.id).exists())

    def test_delete_food_ajax_failure(self):
        fake_id = uuid.uuid4()
        response = self.client.post(reverse('dashboard:delete_food', args=[fake_id]))
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'error')

    def test_get_food_detail_success(self):
        response = self.client.get(reverse('dashboard:get_food', args=[self.food.id]))
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['food']['name'], 'Sate Ayam')

    def test_get_food_detail_failure(self):
        fake_id = uuid.uuid4()
        response = self.client.get(reverse('dashboard:get_food', args=[fake_id]))
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'error')