from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Profile

# Create your tests here.
class URLTests(TestCase):
        
    def test_testlogin(self):
        response = self.client.get('/accounts/userlogin/')
        self.assertEqual(response.status_code,200)
        
    def test_testSignup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)
        
              


class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name='John',
            last_name='Doe',
            dob='1990-01-01',
            email='john@example.com',
            secret_key='12345678',
            phone_number=123456789
        )

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.dob, '1990-01-01')
        self.assertEqual(self.user.email, 'john@example.com')
        self.assertEqual(self.user.secret_key, '12345678')
        self.assertEqual(self.user.phone_number, 123456789)

    def test_user_str_method(self):
        self.assertEqual(str(self.user), 'John Doe')

    def test_user_absolute_url(self):
        expected_url = reverse('accounts:account', args=[str(self.user.id)])
        self.assertEqual(self.user.get_absolute_url(), expected_url)
