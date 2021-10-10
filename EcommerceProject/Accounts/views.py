from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .tokens import *
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import *
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

def customer_registerview(request):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            obj=form.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': obj,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
                'token': account_activation_token.make_token(obj),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, ('Please Confirm your email to complete registration.'))
            return redirect('customerlogin')
    template_name = 'Accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)


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
            return redirect('sellerlogin')
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


# def seller_showview(request):
#     usr=Seller.objects.all()
#     print(usr)
#     tempalte_name='Accounts/SellerShow.html'
#     context={'user':usr}
#     return render(request,tempalte_name,context)

def customer_logout_view(request):
    logout(request)
    return redirect('home')


def seller_logout_view(request):
    logout(request)
    return redirect('sellerhome')




# def generateOTP():
#     digits = "0123456789"
#     OTP = ""
#     for i in range(4):
#         OTP += digits[math.floor(random.random() * 10)]
#     return OTP


# def send_otp(request):
#     email = request.GET.get("email")
#     print(email)
#     o = generateOTP()
#     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
#     send_mail('OTP request', o, '<your gmail id>', [email], fail_silently=False, html_message=htmlgen)
#     return HttpResponse(o)

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')