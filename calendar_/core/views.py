from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.contrib.auth import login
from django.shortcuts import render, redirect
from core.forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


@login_required(login_url='/login/')
def home(request):
   return render(request,'home.html',{'name':request.user.first_name})

 
def sign_up(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('home')
   else:
       form = SignUpForm()
   return render(request,'signup.html',{'form':form})

def log_out(request):
  logout(request)
  return HttpResponse("Thanks for visiting...")

def log_in(request):
   if request.method == 'POST':
       user=authenticate(request,username=request.POST['username'],
       password=request.POST['password'])
       if user is not None:
           login(request,user)
           return redirect('home')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('login')
   else:
       form = AuthenticationForm()
       return render(request,'login.html',{'form':form})
