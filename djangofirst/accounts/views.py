from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

def signup_page(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('article:list')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})