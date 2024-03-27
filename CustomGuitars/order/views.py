from django.shortcuts import render, get_object_or_404
import os
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas
from django.core.mail import send_mail
from django.shortcuts import render
from order.models import Order

def sender_order_email(order):
    subject = "Order Confirmation"
    customers_email = order.emailAddress
    message = f"Thanks for your order!\n\nOrder Number: {order.id}\nTotal: {order.total}\n\n"
    
    order_items = order.orderitem_set.all()
    
    message += "Order Items:\n"
    for item in order_items:
        message += f"Product: {item.product}, Quantity: {item.quantity}\n"
    
    from_email = "CustomGuitars@test.com"
    to_email = [customers_email]

    send_mail(subject, message, from_email, to_email)

def thanks(request, order_id):
    customer_order = get_object_or_404(Order, id=order_id)
    
    
    sender_order_email(customer_order)
    
    return render(request, 'thanks.html', {'customer_order': customer_order})

def users_orders(request):
    users_orders = Order.objects.filter(user=request.user)

    return render(request, 'orders.html',{'user_orders': users_orders})
