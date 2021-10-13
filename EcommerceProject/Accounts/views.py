from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import math, random
from django.views.generic import View
from django.contrib.auth import login, update_session_auth_hash
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail


def customer_registerview(request):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emailverify')
    template_name = 'Accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)



def email_verification(request):
    return render(request, 'Accounts/Email_verification.html')



def customuser_activation(request):
    try:
        email=request.POST.get('email')
        print("Entered Email:    ",email)
        user=CustomUser.objects.get(email=email)
        user.is_active=True
        print("Database User   ",user.email)
        user.save()
        if user.is_customer==True:
            return redirect('customerlogin')
        else:
            return redirect('sellerlogin')
    except CustomUser.DoesNotExist:
        return redirect('sellerlogout')





def customer_loginview(request):
    try:
        if request.method == 'POST':
            no = request.POST.get('mobile')
            p = request.POST.get('password')
            try:
                customer=CustomUser.objects.get(mobile_no=no)
            except CustomUser.DoesNotExist:
                messages.error(request,"Please check mobile no, this No is not registered ")
                return redirect('customerlogin')
            if customer.is_active==True:
                user=authenticate(username=no,password=p)
                if user and user.is_customer:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid Credentials!')
                    return redirect('customerlogin')
            else:
                messages.error(request, 'Your Account is not activated yet, please provide email to activate')
                return redirect('emailverify')
        
        template_name = 'Accounts/login.html'
        context = {}
        return render(request, template_name, context)
    except Customer.DoesNotExist:
        return redirect('logout')


def seller_registerview(request):
    form = SellerCreationForm()
    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emailverify')
    template_name = 'Accounts/sellerregister.html'
    context = {'form': form}
    return render(request, template_name, context)


def seller_loginview(request):
    try:
        if request.method == 'POST':
            no=request.POST.get('mobile')
            p=request.POST.get('password')
            try:
                seller=CustomUser.objects.get(mobile_no=no)
            except CustomUser.DoesNotExist:
                messages.error(request,"Please check mobile no, this No is not registered ")
                return redirect('customerlogin')
            if seller.is_active:
                user=authenticate(username=no,password=p)
                if user and user.is_seller:
                    login(request,user)
                    return redirect('addproduct')
                else:
                    messages.error(request,'Invalid Credentials!')
                    return redirect('sellerlogin')
            else:
                messages.error(request,'Your Account is not activated yet, please provide email to activate')
                return redirect('emailverify')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')
    
    template_name='Accounts/SellerLogin.html'
    context={}
    return render(request,template_name,context)

def customer_logout_view(request):
    logout(request)
    return redirect('home')


def seller_logout_view(request):
    logout(request)
    return redirect('sellerhome')


@login_required(login_url='customerlogin')
def change_pass_view_customer(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Updated Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Check the fields')

    template_name = 'Customer/changepassword.html'
    context = {'form': form}
    return render(request, template_name, context)




@login_required(login_url='customerlogin')
def change_pass_view_seller(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Updated Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Check the fields')

    template_name = 'Seller/changepassword.html'
    context = {'form': form}
    return render(request, template_name, context)




def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(request):
    email = request.POST.get("email")
    print(email)
    try:
        print("From Try ",email)
        CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        messages.error(request,"This Email Id is not registered ")
        return redirect('emailverify')
    print(email)
    o = generateOTP()
    print(o)
    htmlgen = 'Your OTP is '+ o
    print(htmlgen)
    send_mail('OTP request', o, 'kusumdipke@gmail.com', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)


