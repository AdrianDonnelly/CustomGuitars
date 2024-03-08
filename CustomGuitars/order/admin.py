from django.contrib import admin
from .models import Order, OrderItem
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas

class OrderItemAdmin(admin.TabularInline):
        model = OrderItem
        fieldsets = [
        ('Product',{'fields':['product'],}),
        ('Quantity',{'fields':['quantity'],}),
        ('Price',{'fields':['price'],}),
        ] 
        readonly_fields = ['product','quantity','price'] 
        can_delete= False
        max_num = 0

class OrderAdmin(admin.ModelAdmin):
    actions = ['generate_pdf']
    
    def generate_pdf(modeladmin, request, queryset):
    
    
        for order in queryset:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="Order_{order.id}_Report.pdf"'
            
            p = canvas.Canvas(response)
            pdf_title = f'Order {order.id} Details'
            p.setTitle(pdf_title)

            heading = 'ORDER DETAILS'
            p.drawString(250, 800, heading)
            
            order_info = [
                f'Order ID: {order.id}',
                f'Total: {order.total}',
                f'Created: {order.created.strftime("%d-%m-%y %H:%M:%S")}',
                '',
            ]


            billing_info = [
                'BILLING INFORMATION',
                f'Name: {order.billingName}',
                f'Address: {order.billingAddress1}, {order.billingCity}, {order.billingPostcode}, {order.billingCountry}',
                f'Email: {order.emailAddress}',
                '',
            ]


            shipping_info = [
                'SHIPPING INFORMATION',
                f'Name: {order.shippingName}',
                f'Address: {order.shippingAddress1}, {order.shippingCity}, {order.shippingPostcode}, {order.shippingCountry}',
                '',
            ]


            order_items = ['ORDER ITEMS']
            for item in order.orderitem_set.all():
                order_items.extend([
                    f'Product: {item.product}',
                    f'Quantity: {item.quantity}',
                    f'Price: {item.price}',
                    '',
                ])

            full_info = order_info + billing_info + shipping_info + order_items

            y_position = 750
            for line in full_info:
                p.drawString(110, y_position, line)
                y_position -= 20 

            pdf_file_path = f'static/pdf/order_{order.id}.pdf'
            p.save()
            with open(pdf_file_path, 'wb') as pdf_file:
                pdf_file.write(response.content)

        return response
    
    generate_pdf.short_description = "Generate PDFs"
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = ['id','billingName','emailAddress','created']##order admin preview
    
    list_display_links = ('id','billingName') 
    search_fields = ['id','billingName','emailAddress'] 
    readonly_fields = ['id','token','total','emailAddress','created','billingName','billingAddress1','billingCity', 'billingPostcode','billingCountry','shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry'] 
    fieldsets = [
    ('ORDER INFORMATION',{'fields': ['id','token','total','created']}),
    ('BILLING INFORMATION', {'fields': ['billingName','billingAddress1','billingCity','billingPostcode','billingCountry','emailAddress']}),
    ('SHIPPING INFORMATION', {'fields': ['shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
 ] 
 
    inlines = [
        OrderItemAdmin
 ] 
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False

admin.site.register(Order, OrderAdmin)