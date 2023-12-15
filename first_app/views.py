from django.shortcuts import render, redirect
from .forms import SignUp
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request,'home.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('profile')
    else:
        form = SignUp()
    return render(request,'in&out.html',{'form':form, 'type': 'SignUP'})

def user_profile(request):
    return render(request,'profile.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,"Logged in to account Successfully")
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request,"At first creat an account")
                return redirect('signup_page')
    else:
        form = AuthenticationForm()
        return render(request,'in&out.html',{'form':form, 'type': 'Login'})


def user_logout(request):
    logout(request)
    return redirect('login_page')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Changed sucessfully")
            return redirect('logout_page')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,'in&out.html',{'form':form})