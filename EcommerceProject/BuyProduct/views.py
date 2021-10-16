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
from datetime import date
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
            # obj.order_date=date.today()
            print("mobile in stock before adding order",mobileitem.stock)
            mobileitem.stock-=1
            mobileitem.save()
            print("mobile in stock after adding order",mobileitem.stock)
            if form.cleaned_data['payment_mode']=='Cash on delivery':
                obj.save()
                print('Order Placed!!!')
                return redirect('myorder')
            else:
                obj.save()
                return redirect('customerrazorpay')
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
# def buy_cart_product(request):
#     customer=Customer.objects.get(user=request.user)
#     all_products=Cart.objects.filter(customer=customer)
#     form=OrderedProductForm()
#     if request.method=='POST':
#         form=OrderedProductForm(request.POST)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.customer=customer
#             obj.mobile=mobileitem
#             obj.price=mobileitem.price
#             obj.quantity=1
#             obj.order_date=datetime.now().strftime("%H%M%S%m%d%Y"),
#             print("mobile in stock before adding order",mobileitem.stock)
#             mobileitem.stock-=1
#             mobileitem.save()
#             print("mobile in stock after adding order",mobileitem.stock)
#             obj.save()
#             print('Order Placed!!!')
#         return redirect('myorder')
#     template_name='BuyProduct/BuyItem.html'
#     context={'form':form,'mobile':mobileitem}
#     return render(request,template_name,context)





@login_required(login_url='customerlogin')
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