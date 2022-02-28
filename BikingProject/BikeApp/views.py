from django.shortcuts import render, redirect
from .models import *
form django.contrib import messages
import bcrypt

def home(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, 'index.html')

def grouprides(request):
    
    return render(request, 'grouprides.html')