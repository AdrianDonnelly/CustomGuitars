from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class URLTests(TestCase):
    def test_testhome(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
        
from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
        name='Cat_Test',
    )
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Cat_Test')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Cat_Test')

    def test_category_get_absolute_url(self):
        expected_url = reverse('shop:products_by_category', args=[str(self.category.id)])
        self.assertEqual(self.category.get_absolute_url(), expected_url)
        
class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Product_Test')

        self.product = Product.objects.create(
            name='Product_Test',
            description='TEST TEST',
            category=self.category,
            price=99.99,
            stock=20,
            available=True)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Product_Test')
        self.assertEqual(self.product.description, 'TEST TEST')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.price, 99.99)
        self.assertEqual(self.product.stock, 20)
        self.assertTrue(self.product.available)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Product_Test')

    def test_product_get_absolute_url(self):
        expected_url = reverse('shop:product_detail', args=[str(self.category.id), str(self.product.id)])
        self.assertEqual(self.product.get_absolute_url(), expected_url)