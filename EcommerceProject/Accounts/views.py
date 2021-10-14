from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def customer_registerview(request, account_activation_token=None):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.is_active=False
            obj.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('acc_active_email.html', {
            #     'user': obj,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
            #     'token': account_activation_token.make_token(obj),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            # email.send()
            return redirect('customerlogin')
    template_name = 'Accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)


def customer_loginview(request):
    logout(request)
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


def customer_logout_view(request):
    logout(request)
    return redirect('customerlogin')



def seller_registerview(request):
    form = SellerCreationForm()
    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellerlogin')
    template_name = 'Accounts/sellerregister.html'
    context = {'form': form}
    return render(request, template_name, context)


def seller_loginview(request):
    logout(request)
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


def seller_logout_view(request):
    logout(request)
    return redirect('sellerlogin')


@login_required(login_url='customerlogin')
def change_pass_view(request):
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

    template_name = 'Accounts/changepassword.html'
    context = {'form': form}
    return render(request, template_name, context)


# def generateOTP():
#     digits = "0123456789"
#     OTP = ""
#     for i in range(4):
#         OTP += digits[math.floor(random.random() * 10)]
#     return OTP
#
#
# def send_otp(request):
#     email = request.GET.get("email")
#     print(email)
#     o = generateOTP()
#     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
#     send_mail('OTP request', o, '<your gmail id>', [email], fail_silently=False, html_message=htmlgen)
#     return HttpResponse(o)