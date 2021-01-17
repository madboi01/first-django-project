from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def signup_page(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            #log user in
            return redirect('article:list')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_page(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user in
            user=form.get_user()
            login(request,user)
            return redirect('article:list')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})