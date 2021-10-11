from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import math, random
from django.views.generic import View
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

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
    email=request.POST.get('email')
    print(email)
    user=CustomUser.objects.get(email=email)
    # print(customer)
    user.is_active=True
    user.save()
    if user.is_customer==True:
        return redirect('customerlogin')
    else:
        return redirect('sellerlogin')





def customer_loginview(request):
    if request.method == 'POST':
        no = request.POST.get('mobile')
        p = request.POST.get('password')
        user = authenticate(username=no, password=p)
        if user and user.is_customer:
            login(request, user)
            return redirect('home')
        messages.error(request, 'You are not a customer')
    template_name = 'Accounts/login.html'
    context = {}
    return render(request, template_name, context)


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
    if request.method == 'POST':
        no = request.POST.get('mobile')
        p = request.POST.get('password')
        user = authenticate(username=no, password=p)
        if user and user.is_seller:
            login(request, user)
            return redirect('addproduct')
        messages.error(request, 'You are not a Seller')
    template_name = 'Accounts/SellerLogin.html'
    context = {}
    return render(request, template_name, context)

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
    o = generateOTP()
    print(o)
    htmlgen = 'Your OTP is '+ o
    send_mail('OTP request', o, 'kusumdipke@gmail.com', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)


