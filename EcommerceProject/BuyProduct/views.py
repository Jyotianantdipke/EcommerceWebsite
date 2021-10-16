from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from reportlab.pdfbase.pdfmetrics import Encoding
from Accounts.models import Customer
from Seller.models import Mobile,Laptop,Grocery
from.models import OrderedProduct
from Customer.models import Cart
from .models import OrderedProduct
from .forms import OrderedProductForm
import io
from datetime import datetime
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

@login_required(login_url='customerlogin')
def buynow_mobile(request,id):
    mobileitem=Mobile.objects.get(id=id)
    user = request.user
    customer = Customer.objects.get(user=user)
    form=OrderedProductForm()
    if request.method=='POST':
        form=OrderedProductForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.customer=customer
            obj.mobile=mobileitem
            obj.price=mobileitem.price
            obj.quantity=1
            obj.order_date=datetime.datetime.now().strftime("%H%M%S%m%d%Y"),
            print("mobile in stock before adding order",mobileitem.stock)
            mobileitem.stock-=1
            mobileitem.save()
            print("mobile in stock after adding order",mobileitem.stock)
            obj.save()
            print('Order Placed!!!')
        return redirect('myorder')
    template_name='BuyProduct/BuyItem.html'
    context={'form':form,'mobile':mobileitem}
    return render(request,template_name,context)
   
@login_required(login_url='customerlogin')
def my_order(request):
    customer=Customer.objects.get(user=request.user)
    order=OrderedProduct.objects.filter(customer=customer)
    context={'order':order}

    for i in order:
        print(i.customer)
        print(i.mobile.name)
    template_name='BuyProduct/MyOrder.html'
    return render(request,template_name,context)


# @login_required(login_url='customerlogin')
# def buynow_laptop(request,id):
#     laptopitem=Mobile.objects.get(id=id)
#     user = request.user
#     try:
#         customer = Customer.objects.get(user=user)
#         y = OrderedProduct.objects.filter(customer=customer, laptop=OrderedProduct).first()
#         if y:
#             z = y.quantity + 1
#             p = y.price / y.quantity
#             q = p * z
#             y.price = q
#             y.quantity = z
#             y.save()
#             print('Updated!!!')
#             return redirect('myorder')
#         else:
#             OrderedProduct.objects.create(customer=customer, laptop=laptopitem, mobile=None, grocery=None, price=laptopitem.price, quantity=1)
#             print('Order Placed!!!')
#         return redirect('myorder')
#     except Customer.DoesNotExist:
#         return redirect('customerlogin')


# @login_required(login_url='customerlogin')
# def buynow_grocery(request,id):
#     groceryitem=Mobile.objects.get(id=id)
#     user = request.user
#     try:
#         customer = Customer.objects.get(user=user)
#         y = OrderedProduct.objects.filter(customer=customer, grocery=OrderedProduct).first()
#         if y:
#             z = y.quantity + 1
#             p = y.price / y.quantity
#             q = p * z
#             y.price = q
#             y.quantity = z
#             y.save()
#             print('Updated!!!')
#             return redirect('myorder')
#         else:
#             OrderedProduct.objects.create(customer=customer, laptop=None, mobile=None, grocery=groceryitem, price=groceryitem.price, quantity=1)
#             print('Order Placed!!!')
#         return redirect('myorder')
#     except Customer.DoesNotExist:
#         return redirect('customerlogin')

# @login_required(login_url='customerlogin')
# def buynow_cartproduct(request):
#     customer=Customer.objects.get()
#     record=OrderedProduct.objects.filter(customer=customer)
#     context={'record':record}
#     for i in record:
#         if i.laptop_id is not None:
#             product_id = i.laptop_id
#             product_name_l = Laptop.objects.get(id=product_id)
#             context['product_name_l']=product_name_l.name
#             print("Laptop", product_name_l.name)
#         elif i.mobile_id is not None:
#             product_id = i.mobile_id
#             product_name_m = Mobile.objects.get(id=product_id)
#             print("Mobile", product_name_m.name)
#             context['product_name_m']=product_name_m
#         elif i.grocery_id is not None:
#             product_id = i.grocery_id
#             product_name_g = Grocery.objects.get(id=product_id)
#             print("Mobile", product_name_g)
#             context['product_name_g']=product_name_g
#             print(product_id)





def create_Invoice(request,id):
    # Create a file-like buffer to receive PDF data.
    order=OrderedProduct.objects.get(id=id)
    customer=Customer.objects.get(user=request.user)
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50,820,"Order Details")
    p.drawString(50,800,str(order.customer))
    p.drawString(50,780,str(order.mobile))
    p.drawString(50,760,str(order.quantity))
    p.drawString(50,740,str(order.delivery_address))
    p.drawString(50,720,str(order.payment_mode))


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    
    return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')