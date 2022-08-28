from django.shortcuts import render, redirect
from django.http import HttpResponse

from account.forms import RegistrationForm, ProfileFrom

# authentication function
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from order.models import Cart, Order
from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from account.models import Profile

from django.views.generic import TemplateView

def register(request):
    if request.user.is_authenticated:
        return HttpResponse("You are In")
    else:
        form = RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            print("This is nothing")
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return HttpResponse("Your Account has been created")
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def customer_login(request):
    if request.user.is_authenticated:
        return HttpResponse("You are logged in")
    else:
        if request.method == 'post' or request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(request, username=username, password=password)
            if customer is not None:
                login(request, customer)
                return HttpResponse("You are logged In successfully")
            else:
                return HttpResponse("404")
    return render(request, 'login.html')

#Customer Profile


class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user, ordered=True) 
        billingaddress = BillingAddress.objects.get(user=request.user)

        billingaddress_form = BillingAddressForm(instance=billingaddress)
        profile_obj = Profile.objects.get(user=request.user)
        profile_form = ProfileFrom(instance=profile_obj)
        context = {
            'orders': orders,
            'billingaddress': billingaddress_form,
            'profileForm': profile_form,
        }
        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            billingaddress = BillingAddress.objects.get(user=request.user)
            billingaddress_form = BillingAddressForm(request.POST, instance=billingaddress)
            profile_obj = Profile.objects.get(user=request.user)
            profile_form = ProfileFrom(request.POST, instance=profile_obj)
            if billingaddress_form.is_valid() or profile_form.is_valid():
                billingaddress_form.save()
                profile_form.save()
                return redirect('account:profile')
            
