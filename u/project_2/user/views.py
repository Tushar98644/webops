from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def register(request):
   if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']

     user=authenticate(request,username=username,password=password)

     if user is not None:
      login(request,user)
      messages.success(request,"valid cerendtials")
      return redirect('/project/project-3')
        
     

     else:
      messages.error(request,"bad cerendtials")
      return redirect('/project/project-3')

   return render (request,'project-2.html')
    
   