from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from vouchers.models import Voucher
from django.core.mail import send_mail
from accounts.models import CustomUser
from twilio.rest import Client



class Order(models.Model):
 user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,)
 token = models.CharField(max_length=250, blank=True) 
 total = models.IntegerField(verbose_name='Euro Order Total') 
 emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address') 
 created = models.DateTimeField(auto_now_add=True) 
 billingName = models.CharField(max_length=250, blank=True) 
 billingAddress1 = models.CharField(max_length=250, blank=True) 
 billingCity = models.CharField(max_length=250, blank=True) 
 billingPostcode = models.CharField(max_length=10, blank=True) 
 billingCountry = models.CharField(max_length=200, blank=True) 
 shippingName = models.CharField(max_length=250, blank=True) 
 shippingAddress1 = models.CharField(max_length=250, blank=True) 
 shippingCity = models.CharField(max_length=250, blank=True) 
 shippingPostcode = models.CharField(max_length=10, blank=True) 
 shippingCountry = models.CharField(max_length=200, blank=True) 
 voucher = models.ForeignKey(Voucher, 
 related_name='orders', 
 null=True, 
 blank=True, 
 on_delete=models.SET_NULL)
 discount = models.IntegerField(default = 0, 
 validators=[MinValueValidator(0), 
 MaxValueValidator(100)])

 

class Meta: 
    db_table = 'Order'
    ordering = ['-created'] 
    
def __str__(self):
    return str(self.id)

def sender_order_email(self):
        subject = "Order Confirmation"
        customers_email = self.emailAddress
        message = f"Thanks for your order!\n\nOrder Number: {self.id}\nTotal: {self.total}\n\n"
        from_email = "CustomGuitars@test.com"
        to_email = [customers_email]

        send_mail(subject, message, from_email, to_email)
    
def whatsapp_order(self):
    account_sid = "AC35862d2a87f33839b12634c64f4e1e9b"
    auth_token  = "56d28fbe8fd7bd44450093c716229d82"
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="whatsapp:+353851765118",
        from_="whatsapp:+15017250604",
        body=f"Thanks for your order!\n\nOrder Number: {self.id}\nTotal: {self.total}\n\n")

    print(message.sid)


class OrderItem(models.Model):
    product = models.CharField(max_length=250) 
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price') 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
 
    class Meta: 
        db_table = 'OrderItem'
 
    def sub_total(self):
        return self.quantity * self.price
 
    def __str__(self):
        return self.product