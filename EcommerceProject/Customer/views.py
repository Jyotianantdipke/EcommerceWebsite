from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Accounts.models import Customer

from .forms import CustomerProfileForm
from .models import Cart, State, City
from django.contrib.auth.decorators import login_required
from Seller.models import Laptop, Mobile, Grocery

# Create your views here.
from Seller.filters import LaptopFilter, MobileFilter, GroceryFilter


def showlaptop(request):
    records = Laptop.objects.all()
    laptopfilter = LaptopFilter(request.GET, queryset=records)
    rec_per_page = Paginator(laptopfilter.qs, 3)
    page = request.GET.get('page',1)
    # print('PAGE=',page)
    # print(rec_per_page.count)
    # print(rec_per_page.num_pages)
    # print(rec_per_page.page_range)
    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)
    print('filter record', records)
    return render(request, 'Customer/ShowLaptop.html', {'records': rec, 'laptopfilter': laptopfilter})


def showMobile(request):
    records = Mobile.objects.all()
    mobilefilter = MobileFilter(request.GET, queryset=records)
    rec_per_page = Paginator(mobilefilter.qs, 3)
    print('PAGINATOR=', rec_per_page)
    page = request.GET.get('page', 1)
    print('PAGE=', page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)
    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request, 'Customer/ShowMobile.html', {'records': rec,'mobilefilter':mobilefilter})


def showGrocery(request):
    records = Grocery.objects.all()
    groceryfilter = GroceryFilter(request.GET, queryset=records)
    rec_per_page = Paginator(groceryfilter.qs, 3)
    print('PAGINATOR=', rec_per_page)
    page = request.GET.get('page', 1)
    print('PAGE=', page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request, 'Customer/ShowGrocery.html', {'records': rec,'groceryfilter':groceryfilter})

@login_required(login_url='customerlogin')
def Laptopview(request, pk):
    laptop = Laptop.objects.get(id=pk)
    user = request.user
    print('User :', user.id)
    cst = Customer.objects.get(user=user)
    y = Cart.objects.filter(customer=cst, laptop=laptop).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('showcart')
    else:
        Cart.objects.create(customer=cst, laptop=laptop, mobile=None, grocery=None, price=laptop.price, quantity=1)
        print('Created!!!')
    return redirect('showcart')


def Mobileview(request, pk):
    mobile = Mobile.objects.get(id=pk)
    user = request.user
    cst = Customer.objects.get(user=user)
    y = Cart.objects.filter(customer=cst, mobile=mobile).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('showcart')
    else:
        Cart.objects.create(customer=cst, laptop=None, mobile=mobile, grocery=None, price=mobile.price, quantity=1)
        print('Created!!!')
    return redirect('showcart')


@login_required(login_url='customerlogin')
def show_cart(request):
    customer = Customer.objects.get(user=request.user)
    cart_data = Cart.objects.filter(customer=customer)
    # print('Cart Data', cart_data)
    # for i in cart_data:
    #     print(i.laptop_id)
    #     for k in i:
    #         print(k.name)
    context = {'cart_data': cart_data}

    template_name = 'Customer/ShowCart.html'
    return render(request, template_name, context)


@login_required(login_url='customerlogin')
def shop_now(request):
    context = {}
    template_name = 'Customer/ShopNow.html'
    return render(request, template_name, context)


def Groceryview(request, pk):
    grocery = Grocery.objects.get(id=pk)
    user = request.user
    cst = Customer.objects.get(user=user)
    y = Cart.objects.filter(customer=cst, grocery=grocery).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('showcart')
    else:
        Cart.objects.create(customer=cst, laptop=None, mobile=None, grocery=grocery, price=grocery.price, quantity=1)
        print('Created!!!')
    return redirect('showcart')


@login_required(login_url='customerlogin')
def Cartview(request):
    user = request.user
    print('User:', user)
    cst = Customer.objects.get(user=user)
    print(cst)
    ord = Cart.objects.filter(customer=cst)
    for i in ord:
        if i.laptop_id is not None:
            product_id = i.laptop_id
            product_name_l = Laptop.objects.get(id=product_id)
            print("Laptop", product_name_l.name)
        elif i.mobile_id is not None:
            product_id = i.mobile_id
            product_name_m = Mobile.objects.get(id=product_id)
            print("Mobile", product_name_m.name)
        elif i.grocery_id is not None:
            product_id = i.grocery_id
            product_name_g = Grocery.objects.get(id=product_id)
            print("Mobile", product_name_g)
            print(product_id)
    template_name = 'Customer/showCart.html'
    context = {'ord': ord, 'product_name_m': product_name_m.name, 'product_name_l': product_name_l.name}
    return render(request, template_name, context)


@login_required(login_url='login')
def Deleteitemview(request, pk):
    # item=Order_item.objects.get(id=pk)
    # item.delete()
    # return redirect('cartview')
    y = Cart.objects.get(id=pk)
    if y.quantity > 1:
        z = y.quantity - 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('showcart')
    else:
        print('Deleted!!')
        y.delete()
    return redirect('showcart')


def Updateallitemview(request, pk):
    y = Cart.objects.filter(id=pk).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('showcart')



@login_required(login_url='customerlogin')
def create_profile_view(request):
    customer = Customer.objects.get(user=request.user)
    form = CustomerProfileForm()
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = customer
            obj.address=form.cleaned_data['flat']+', '+form.cleaned_data['area']+', '+form.cleaned_data['landmark']
            obj.save()
            return redirect('viewprofile')
    template_name = 'Customer/Customerprofile.html'
    context = {'form': form}
    return render(request, template_name, context)


# AJAX

def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id)
    context = {'states': states}
    return render(request, 'Customer/Statelist.html', context)


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id)
    context = {'cities': cities}
    return render(request, 'Customer/citylist.html', context)





def universal_search_view(request):
    context={}
    search_query=request.POST.get('search_query')
    laptop_record=Laptop.objects.filter(Q(name__unaccent__lower__trigram_similar=search_query))
                  # | Laptop.objects.filter(name__unaccent__lower__trigram_similar='Dell')|Laptop.objects.filter(name__unaccent__lower__trigram_similar='Lenovo')|Laptop.objects.filter(name__unaccent__lower__trigram_similar='Apple')
    # grocery_record=Grocery.objects.filter(name__unaccent__lower__trigram_similar='')
    mobile_record=Mobile.objects.filter(name__unaccent__lower__trigram_similar='redmi')
    # Mobile.objects.filter(name__unaccent__lower__trigram_similar='vivo') | Mobile.objects.filter(name__unaccent__lower__trigram_similar='Apple') | Mobile.objects.filter(name__unaccent__lower__trigram_similar='oppo')
    if laptop_record:
        context['laptop_record']=laptop_record
    if mobile_record:
        context['mobile_record']=mobile_record
    template_name='Customer/search_result.html'
    return render(request,template_name, context)