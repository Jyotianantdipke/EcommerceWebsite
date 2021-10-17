from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Accounts.models import Customer
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
    print(len(all_products))
    for i in all_products:
        print(i.id,i.price,type(i))
    form=OrderedProductForm()
    if request.method=='POST':
        form=OrderedProductForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.customer=customer
            for i in Cart.objects.filter(customer=customer):
                print('inside for')
                if i.mobile is not None:
                    mobileitem=Mobile.objects.get(id=i.mobile.id)
                    print(mobileitem)
                    obj.mobile=i.mobile
                    obj.quantity=i.quantity
                    obj.price=i.price
                    i.delete()
                    obj.save()
                    mobileitem.stock-=i.quantity
                elif i.laptop is not None:
                    laptopitem=Laptop.objects.get(id=i.laptop.id)
                    obj.laptop=i.laptop
                    obj.quantity=i.quantity
                    obj.price=i.price
                    obj.save()
                    i.delete()
                    laptopitem.stock-=i.quantity
                elif i.grocery is not None:
                    grocreyitem=Grocery.objects.get(id=i.grocery.id)
                    obj.grocery=i
                    obj.quantity=i.quantity
                    obj.price=i.price
                    obj.save()
                    i.delete()
                    grocreyitem.stock-=i.quantity      
            if form.cleaned_data['payment_mode']=='Cash on Delivery':
                print("inside if mode of payment", form.cleaned_data['payment_mode'])
                print('Order Placed!!!')
                return redirect('myorder')
            else:
                print("inside else mode of payment", form.cleaned_data['payment_mode'])
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
        "mobile" :order.mobile,
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




