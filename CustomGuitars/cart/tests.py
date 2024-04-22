from django.test import TestCase
from .models import Cart, CartItem
from shop.models import Product, Category


# Create your tests here.
class URLTests(TestCase):
        
    def test_testcart(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)



class CartModelTest(TestCase):

    def setUp(self):
        self.cart = Cart.objects.create(cart_id='test_cart')

    def test_cart_creation(self):
        self.assertEqual(self.cart.cart_id, 'test_cart')

    def test_cart_str_method(self):
        self.assertEqual(str(self.cart), 'test_cart')
class CartItemModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Product_Category'
        )

        self.product = Product.objects.create(
            name='Product_Test',
            description='TEST TEST',
            category=self.category,
            price=99.99,
            stock=20,
            available=True
        )
        self.cart = Cart.objects.create(cart_id='test_cart')
        self.cart_item = CartItem.objects.create(
            product=self.product,
            cart=self.cart,
            quantity=2
        )

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertTrue(self.cart_item.active)

    def test_cart_item_sub_total(self):
        expected_subtotal = self.product.price * self.cart_item.quantity
        self.assertEqual(self.cart_item.sub_total(), expected_subtotal)

    def test_cart_item_str_method(self):
        self.assertEqual(str(self.cart_item), str(self.product))
