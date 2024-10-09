from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_page(self):
        response = Client().get('/notfoundpage/')
        self.assertEqual(response.status_code, 404)
