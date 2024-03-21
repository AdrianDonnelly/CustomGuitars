from django.test import TestCase


# Create your tests here.
class URLTests(TestCase):
        
    def test_testlogin(self):
        response = self.client.get('/accounts/userlogin/')
        self.assertEqual(response.status_code,200)
        
    def test_testSignup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)
        
        