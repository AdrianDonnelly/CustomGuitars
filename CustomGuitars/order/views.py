from django.shortcuts import render, get_object_or_404
import os
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas
from django.core.mail import send_mail
from django.shortcuts import render
from order.models import Order
from django.conf import settings
from twilio.rest import Client



def sender_order_email(order):
    subject = "Order Confirmation"
    recipient = order.emailAddress
    message = f"Thanks for your order!\n\nOrder Number: {order.id}\nTotal: {order.total}\n\n"
    
    order_items = order.orderitem_set.all()
    
    message += "Order Items:\n"
    for item in order_items:
        message += f"Product: {item.product}, Quantity: {item.quantity}\n"
        
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient],fail_silently=False)
    
# def whatsapp_order(order):
#     account_sid = "AC35862d2a87f33839b12634c64f4e1e9b"
#     auth_token  = "56d28fbe8fd7bd44450093c716229d82"
    
#     phone_number = order.user.phone_number
#     formatted_phone_number = f"whatsapp:+353{phone_number}"
    
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         to= formatted_phone_number,
#         from_="whatsapp:+14155238886",
#         body=f"Thanks for your order!\n\nOrder Number: {order.id}\nTotal: {order.total}\n\n")

# def sms_order(order):
#     account_sid = "AC35862d2a87f33839b12634c64f4e1e9b"
#     auth_token  = "56d28fbe8fd7bd44450093c716229d82"
    
#     phone_number = order.user.phone_number
#     formatted_phone_number = f"+353{phone_number}"
    
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         to=formatted_phone_number,
#         from_="+12058289417",
#         body=f"Thanks for your order!\n\nOrder Number: {order.id}\nTotal: {order.total}\n\n")
   
def thanks(request, order_id):
    customer_order = get_object_or_404(Order, id=order_id)
    
    
    sender_order_email(customer_order)
    # whatsapp_order(customer_order)
    # sms_order(customer_order)
    
    return render(request, 'thanks.html', {'customer_order': customer_order})

def users_orders(request):
    users_orders = Order.objects.filter(user=request.user)

    return render(request, 'orders.html',{'user_orders': users_orders})
