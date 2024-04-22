from django.test import TestCase
from django.core.mail import outbox
from accounts.models import CustomUser
from .models import Order, OrderItem


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com'
        )
        self.order = Order.objects.create(
            user=self.user,
            total=100,
            emailAddress='john@example.com',
            billingName='John Doe',
            billingAddress1='123 Main St',
            billingCity='Anytown',
            billingPostcode='12345',
            billingCountry='USA',
            shippingName='John Doe',
            shippingAddress1='123 Main St',
            shippingCity='Anytown',
            shippingPostcode='12345',
            shippingCountry='USA',
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.total, 100)
        self.assertEqual(self.order.emailAddress, 'john@example.com')

    # def test_order_str_method(self):
    #     self.assertEqual(str(self.order), '1')

    # def test_sender_order_email(self):
    #     self.order.sender_order_email()
    #     self.assertEqual(len(outbox), 1)
    #     self.assertEqual(outbox[0].subject, "Order Confirmation")
    #     self.assertEqual(outbox[0].to, ['john@example.com'])


class OrderItemModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com'
        )
        self.order = Order.objects.create(
            user=self.user,
            total=100,
            emailAddress='john@example.com',
            billingName='John Doe',
            billingAddress1='123 Main St',
            billingCity='Anytown',
            billingPostcode='12345',
            billingCountry='USA',
            shippingName='John Doe',
            shippingAddress1='123 Main St',
            shippingCity='Anytown',
            shippingPostcode='12345',
            shippingCountry='USA',
        )
        self.order_item = OrderItem.objects.create(
            product='Test Product',
            quantity=2,
            price=50,
            order=self.order
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.product, 'Test Product')
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.order_item.price, 50)
        self.assertEqual(self.order_item.order, self.order)

    def test_order_item_sub_total(self):
        self.assertEqual(self.order_item.sub_total(), 100)

    def test_order_item_str_method(self):
        self.assertEqual(str(self.order_item), 'Test Product')
