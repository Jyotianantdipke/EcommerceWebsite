from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import MobileModelForm, LaptopModelForm, GroceryModelForm
from .models import Laptop, Mobile, Grocery
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import LaptopFilter
from Accounts.models import CustomUser, Seller
from faker import Faker
# import Faker



# Create your views here.
def homeview(request):
    template_name='Accounts/home.html'
    Laptops=Laptop.objects.all()
    Mobiles=Mobile.objects.all()
    Groceries=Grocery.objects.all()

    context={'Laptops':Laptops, 'Mobiles':Mobiles, 'Groceries':Groceries}
    return render(request,template_name,context)

# CRUD for SELLER-LAPTOP
# @login_required(login_url='sellerlogin')
# class LaptopListView(ListView):
#     model = Laptop
#     # filterset_class = LaptopFilter



def AddProductView(request):
    return render(request, 'Seller/AddProduct.html' )


# @login_required(login_url='sellerlogin')
# class LaptopCreateView(CreateView):
#     model = Laptop
#     fields = '__all__'
#     success_url = reverse_lazy('lshow')

@login_required(login_url='sellerlogin')
def createFakeLaptop(request):
    # if request.method=='POST':
        # no=int(request.POST.get('no'))
        # print(type(no))
        seller = Seller.objects.get(user=request.user)
        MODEL=['MacBook air 17','MacBook air 2020', 'MacBook Pro', 'VivoNook15', 'Inspiration 3502', 'Notebook Pro', 'Pavilion']
        BRAND = ['HP', 'Apple', 'Dell', 'Asus', 'Lenovo' 'MI']
        RAM=[4,8,12,16, 32]
        ROM=[256,512, 1024, 2048, 4069]
        PROCESSOR=['i3', 'i5', 'i7', 'AMD Ryzen5', 'i9', 'Intel Core 2', 'AMD Ryzen5', 'Intel Atom' ]
        OS=['Windows', 'Linux', 'MackOS']
        WARRANTY=[1,2,3,5,10]
        Price=[50000, 45000, 56000,67000, 15000,50000, 123000 ]

        fake=Faker()
        for i in range(10):
            m=fake.random_element(MODEL)
            b = fake.random_element(BRAND)
            ra = fake.random_element(RAM)
            ro= fake.random_element(ROM)
            pr = fake.random_element(PROCESSOR)
            os=fake.random_element(OS)
            w = fake.random_element(WARRANTY)
            p=fake.random_element(Price)
            so=fake.random_number(digits=2)
            Laptop.objects.create(seller=seller, name=m,brand_name=b, RAM=ra, ROM=ro, processor=pr, OS=os, warranty=w, price=p, stock=so)
        return redirect('showselleresproduct')






@login_required(login_url='sellerlogin')
def addmobile(request):
    form = MobileModelForm()
    if request.method == 'POST':
        form = MobileModelForm(request.POST)
        if form.is_valid():
            seller_user = Seller.objects.get(user=request.user)
            print(seller_user)
            object = form.save(commit=False)
            object.seller = seller_user
            object.save()
            return redirect('showselleresproduct')
    template_name='Seller/Mobile_form.html'
    context={'form':form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def addgrocery(request):
    form = GroceryModelForm()
    if request.method == 'POST':
        form = GroceryModelForm(request.POST)
        if form.is_valid():
            seller_user = Seller.objects.get(user=request.user)
            print(seller_user)
            object = form.save(commit=False)
            object.seller = seller_user
            object.save()
            return redirect('showselleresproduct')
    template_name='Seller/Grocery_form.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='sellerlogin')
def addlaptop(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            seller_user = Seller.objects.get(user=request.user)
            print(seller_user)
            object = form.save(commit=False)
            object.seller = seller_user
            object.save()
            return redirect('showselleresproduct')
    template_name='Seller/Laptop_form.html'
    context={'form':form}
    return render(request, template_name, context)



@login_required(login_url='sellerlogin')
def createFakeMobile(request):
    # if request.method=='POST':
        # no=int(request.POST.get('no'))
        # print(type(no))
        seller = Seller.objects.get(user=request.user)
        # SELLER = []
        # for i in all_user:
        #     print(' All Seller User:', i.user_id, type(i.user_id))
        #     SELLER.append(i)
        MODEL=['Galaxy 12','9A', 'Galaxy M13', 'Note 10S', 'Note M12', 'S 12 Pro']
        BRAND = ['Vivo', 'iphone', 'MI', 'Samsung', 'Realme' 'OPPO']
        RAM=[4,8,12,16]
        ROM=[32,64,128,256,512]
        PROCESSOR=['Quard Core', 'Hexa Core', 'Octa Core', 'SnapDragon']
        WARRANTY=[1,2,3,5,10]
        Price=[23000, 45000, 56000,67000, 15000,50000 ]


        fake=Faker()
        for i in range(10):
            m=fake.random_element(MODEL)
            b = fake.random_element(BRAND)
            ra = fake.random_element(RAM)
            ro= fake.random_element(ROM)
            pr = fake.random_element(PROCESSOR)
            w = fake.random_element(WARRANTY)
            p=fake.random_element(Price)
            so = fake.random_number(digits=2)
            Mobile.objects.create(seller=seller,name=m,brand_name=b, RAM=ra, ROM=ro, processor=pr, warranty=w, price=p, stock=so)
        return redirect('showselleresproduct')








@login_required(login_url='sellerlogin')
def createFakeGrocery(request):
    # if request.method=='POST':
        # no=int(request.POST.get('no'))
        # print(type(no))
        user=request.user
        print(' Seller User for fake data:', user.id)


        seller = Seller.objects.get(user=request.user)
       
        NAME=['Sugar','Tea Powder', 'Coffee Powder', 'Chana / Chole', 'Red Rajma','Rosted Suji (Rava)']
        Price=[23, 45, 56]
        WARRANTY = [1, 2, 3, 5, 10]
        fake=Faker()
        for i in range(10):
            n=fake.random_element(NAME)
            q = fake.random_number(digits=2)
            p=fake.random_element(Price)
            w = fake.random_element(WARRANTY)
            # s = fake.random_element(SELLER)
            Grocery.objects.create(seller=seller, product_name=n,quantity=q, price=p, warranty=w)
        return redirect('showselleresproduct')







@login_required(login_url='sellerlogin')
def delete_laptop(request,id):
    
    record = Laptop.objects.get(id=id)
    
    record.delete()
    return redirect('showselleresproduct')

@login_required(login_url='sellerlogin')
def delete_mobile(request,id):
    record = Mobile.objects.get(id=id)
    record.delete()
    return redirect('showselleresproduct')

@login_required(login_url='sellerlogin')
def delete_grocery(request,id):
    record = Grocery.objects.get(id=id)
    record.delete()
    return redirect('showselleresproduct')



@login_required(login_url='sellerlogin')
def update_mobile(request, id):
    record = Mobile.objects.get(id=id)
    form = MobileModelForm(instance=record)
    if request.method == 'POST':
        form = MobileModelForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('showsellerproduct')
    template_name = 'Seller/Mobile_form.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def update_laptop(request, id):
    record = Laptop.objects.get(id=id)
    form = LaptopModelForm(instance=record)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('showsellerproduct')
    template_name = 'Seller/Laptop_form.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def update_grocery(request, id):
    record = Laptop.objects.get(id=id)
    form = GroceryModelForm(instance=record)
    if request.method == 'POST':
        form = GroceryModelForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('showsellerproduct')
    template_name = 'Seller/Grocery_form.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def show_product_seller(request):
    user = request.user
    seller=Seller.objects.get(user=user)
    laptop = Laptop.objects.filter(seller=seller)
    mobile = Mobile.objects.filter(seller=seller)
    grocery=Grocery.objects.filter(seller=seller)
    context = {'laptop': laptop,'mobile': mobile,'grocery':grocery}
    template_name = 'Seller/showseller_product.html'
    return render(request, template_name, context)