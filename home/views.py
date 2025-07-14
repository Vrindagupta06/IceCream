from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from .forms import FlavourForm

# Create your views here.
def HomePage(request):
    flavour = request.COOKIES.get('user_flavour')

    # Handle visit count
    visit_count_home = request.session.get('visit_count_home', 0)
    visit_count_home += 1
    request.session['visit_count_home'] = visit_count_home

    return render(request, 'index.html', {
        'flavour': flavour,
        'visit_count_home': visit_count_home,
    })


def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.error(request, "Username or password is incorrect.")
    return render(request,'login.html')

def about(request):
    # return HttpResponse("This is About Page.")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is Services Page.")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is contact Page.")
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def choose_flavour(request):
    if request.method == 'POST':
        form = FlavourForm(request.POST)
        if form.is_valid():
            flavour = form.cleaned_data['flavour']
            response = redirect('show_flavour')
            response.set_cookie('user_flavour', flavour, max_age=900)
            return response
    else:
        form = FlavourForm()
    return render(request, 'choose_flavour.html', {'form': form})

def show_flavour(request):
    flavour = request.COOKIES.get('user_flavour', None)
    return redirect('home')

def services(request):
    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    return render(request, 'services.html', {'visit_count': visit_count})
