from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Accounts.models import Customer
from Customer.models import Addresses
from Seller.models import Mobile,Laptop,Grocery
from.models import OrderedProduct
from Customer.models import Cart
from .models import OrderedProduct
from .forms import OrderedProductForm
import io
from datetime import date
from django.http import HttpResponse
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from .utils import render_to_pdf
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
            if form.cleaned_data['payment_mode']=='Cash on Delivery':
                obj.save()
                print('Order Placed!!!')
                return redirect('myorder')
            else:
                obj.save()
                return redirect('customerrazorpay')
    print(mobileitem.price,"price of mobile")
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
        print(i.mobile)
    template_name='BuyProduct/MyOrder.html'
    return render(request,template_name,context)




@login_required(login_url='customerlogin')
def buy_cart_product(request):
    customer=Customer.objects.get(user=request.user)
    all_products=Cart.objects.filter(customer=customer)
    new_data=[]
    form=OrderedProductForm()
    if request.method=='POST':
        form=OrderedProductForm(request.POST)
        if form.is_valid():
            address=request.POST.get('delivery_address')
            add_id=Addresses.objects.get(id=address)
            payment_mode=request.POST.get('payment_mode')
            for i in all_products:
                if i.laptop:
                    obj=OrderedProduct.objects.create(customer=customer,laptop=i.laptop,price=i.price,quantity=i.quantity,delivery_address=add_id,payment_mode=payment_mode)
                elif i.mobile:
                    obj=OrderedProduct.objects.create(customer=customer,mobile=i.mobile,price=i.price,quantity=i.quantity,delivery_address=add_id,payment_mode=payment_mode)
                else:
                    obj=OrderedProduct.objects.create(customer=customer,grocery=i.grocery,price=i.price,quantity=i.quantity,delivery_address=add_id,payment_mode=payment_mode)
            if form.cleaned_data['payment_mode']=='Cash on Delivery':
                print("inside if mode of payment", form.cleaned_data['payment_mode'])
                print('Order Placed!!!')
                return redirect('myorder')
            else:
                return redirect('customerrazorpay')
        return redirect('myorder')
    template_name='BuyProduct/BuyItem.html'
    context={'form':form,'all_products':all_products}
    return render(request,template_name,context)





@login_required(login_url='customerlogin')
def generate_pdf(request,id):
    order=OrderedProduct.objects.get(id=id)
    customer=Customer.objects.get(user=request.user)
    template = get_template('BuyProduct/invoice.html')

    context = {
        "invoice_id": order.id,
        "customer_name": order.customer,
        'billing_address':order.delivery_address,
        'payment_mode':order.payment_mode
    }
    html = template.render(context)
    pdf = render_to_pdf('BuyProduct/invoice.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")




