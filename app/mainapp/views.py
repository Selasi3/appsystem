from django.shortcuts import  render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .models import Person
from django.urls import reverse
from mainapp.forms import PersonForm
from operator import itemgetter

def register(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:login')
    else:
        form = PersonForm()
        return render(request, 'mainapp/register.html', {'form':form})
   
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                print("good")
                # login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('mainapp:upload')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"mainapp/login.html",{"form":form})
   
def uploadfile(request):
    return render(request, "mainapp/upload.html")

def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("mainapp:index")
 