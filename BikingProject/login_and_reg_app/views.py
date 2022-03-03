from django.shortcuts import render, redirect, HttpResponse
from .models import *
import bcrypt
from django.contrib import messages
from .forms import UploadFileForm




# Create your views here.
def loginUser(request):
    return render(request, 'loginUser.html')

def registerUser(request):
    return render(request, 'registerUser.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect("/registerUser")
        else:
            print(request.POST['password'])
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            newUser = User.objects.create(fName = request.POST['fName'],
            lName = request.POST['lName'], email = request.POST['email'], password = pw_hash)
            print(newUser.lName)
            messages.success(request, "Created a New User, please log in")
            return redirect('/')

def login_success(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return redirect('bike/')
        
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        else:
            loggedUser = User.objects.get(email = request.POST['email']) 
            request.session['user'] = loggedUser.id
            return redirect('/login_success')

def log_out(request):
    request.session.flush()
    return redirect('/')

