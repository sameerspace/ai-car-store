

from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserDetails, Vehicle, VehicleImage


# Create your views here.


@login_required
def index(request):
    ctx = {
        'cars': [],
    }
    for vehicle in Vehicle.objects.all():
        item = {
            'vehicle': vehicle,
            'images': [img.image.url for img in VehicleImage.objects.filter(car=vehicle)]
        }
        ctx['cars'].append(item)
    return render(request, 'my_app/index.html', ctx)


def view_all(request):
    if request.POST:
        searchtext = request.POST.get('search')
        if(request.POST.get('city') != 'City'):
            pass
    ctx = {
        'cars': [],
    }
    for vehicle in Vehicle.objects.all():
        item = {
            'vehicle': vehicle,
            'images': [img for img in VehicleImage.objects.filter(car=vehicle)]
        }
        ctx['cars'].append(item)
    return render(request, 'my_app/view_all.html', ctx)


def post_ad(request):
    return render(request, 'my_app/post_ad.html')


def calculate_price(request):
    return render(request, 'my_app/calculate.html')


def user_login(request):
    if request.method == 'POST':
        try:
            uname = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=uname, password=password)
            if user:
                login(request, user)
                return render(request, 'my_app/index.html')
            else:
                print("Wrong Credentials")
                return render(request, 'my_app/login.html')
        except KeyError:
            return render(request, 'my_app/login.html')

    return render(request, 'my_app/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'my_app/login.html')


def signup(request):
    if request.POST:
        try:
            fname = request.POST.get('fname')
            user_email = request.POST.get('email')
            password = request.POST.get('password')
            phonenumber = request.POST.get('phonenumber')
            location = request.POST.get('address')
            user = User.objects.create_user(fname, user_email, password)
            user_detail = UserDetails(
                user_id=user, phone_number=phonenumber, location=location)
            user_detail.save()
            login(request, user)
            return render(request, 'my_app/home.html')
        except KeyError:
            return render(request, 'my_app/register.html')
    return render(request, 'my_app/register.html')
