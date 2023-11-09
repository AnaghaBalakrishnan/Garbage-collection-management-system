from django.shortcuts import render
from typing import Any
from urllib import request
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from account import views
from django.views.generic import TemplateView,CreateView,FormView
from .forms import LogForm,SignUpForm,ContactUsForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.


class SigninView(FormView):
        template_name='signin.html'
        form_class=LogForm
        success_url=reverse_lazy('userh')
        def post(self,request,*args,**kwargs):
             form_data=LogForm(data=request.POST)
             if form_data.is_valid():
                  usn=form_data.cleaned_data.get('username')
                  pas=form_data.cleaned_data.get('password')
                  user=authenticate(request,username=usn,password=pas)
                  if user:
                       login(request,user)
                       return redirect('userh')
                  else:
                       return render(request,'signin.html',{'form':form_data})
                  
             else:
                  return render(request,'signin.html',{'form':form_data})
             
class HomeView(TemplateView):
    template_name='home.html'
     
     # For the contact us form submission.
    def post(self,request,*args,**kwargs):
        name=request.POST.get("name")
        ph=request.POST.get("phone")
        em=request.POST.get("email")
        msg=request.POST.get("message")
        messages.success(self.request,"Message Sent Successfully !")
        ContactUs.objects.create(name=name,phone=ph,email=em,message=msg)
        
        return redirect('h')


class SignUpView(CreateView):
    template_name="signup.html"
    form_class=SignUpForm
    model=User
    success_url=reverse_lazy('signin')
    def form_valid(self,form):
        messages.success(self.request,"Registration Successfull ! Please Sign In  ")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Registration Failed")
        return super().form_invalid(form)

