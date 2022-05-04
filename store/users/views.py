from django.shortcuts import render,HttpResponseRedirect
from users.forms import UserLoginForm,UserRegistrationForm,UserProfileForm
from django.urls import reverse
from django.contrib import auth
# Create your views here.

def login(requests):
    if requests.method == 'POST':
        form = UserLoginForm(data=requests.POST)
        if form.is_valid():
            username = requests.POST['username']
            password = requests.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user and user.is_active:
                auth.login(requests,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(requests,'users/login.html', context)

def register(requests):
    if requests.method == 'POST':
        form = UserRegistrationForm(data=requests.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context= {'form':form}
    return render(requests,'users/register.html', context)

def account(requests):
    if requests.method == 'POST':
        form = UserProfileForm(data=requests.POST,files=requests.FILES,instance=requests.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:account'))
    else:
        form = UserProfileForm(instance=requests.user)
    context = {
        'title': "Account",
        'form' : form,
    }
    return render(requests,'users/account.html',context)
