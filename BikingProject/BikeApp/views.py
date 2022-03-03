from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import bcrypt

def home(request):
    if 'user' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user'])
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)

def grouprides(request):
    user = User.objects.get(id=request.session['user'])
    context = {
        'user': user,
        'rides': Ride.objects.all(),
    }
    return render(request, 'grouprides.html', context)

def groupridedate(request):
    return render(request, 'groupridedate.html')

def joinride(request, id):
    ride = Ride.objects.get(id=id)
    user = User.objects.getg(id=request.session['user'])
    ride.rides_joined.add(user)
    return redirect('home')

def myrides(request):
    user = User.objects.get(id=request.session['user'])
    context = {
        'user': user,
        'rides': Ride.objects.all(),
    }
    return render(request, 'myrides.html', context)

def myaccount(request, id):
    user = User.objects.get(id=request.session['user'])
    context= {
        'user': user,
        'rides': Ride.objects.all(),
    }
    return render(request, 'myaccount.html', context)


def updateaccount(request, id):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/myaccount/' +str(id))
        else:
            userupdate = User.objects.get(id=request.session['user'])
            userupdate.fName = request.POST['fName']
            userupdate.lName = request.POST['lName']
            userupdate.email = request.POST['email']
            userupdate.skill = request.POST['skill']
            userupdate.preferred_ride_distance = request.POST['preferred_ride_distance']
            userupdate.save()
            return redirect()
def gotocreate(request):
    if request.method == 'POST':
        print(request.POST)
        
    return render(request, 'createride.html')

def createride(request):
    if request.method == 'POST':
        uploaded_route = request.FILES['routefile']
        fs = FileSystemStorage()
        fs.save(uploaded_route.name, uploaded_route)
        currentUser = User.objects.get(id=request.session['user'])
        newRide = Ride.objects.create(ridetitle=request.POST['ridetitle'], startingpoint= request.POST['startingpoint'], routefile= uploaded_route, distance=request.POST['distance'], dateofride=request.POST['dateofride'], skill=request.POST['skill'], desc=request.POST['desc'], ride_start_time=request.POST['ride_start_time'], est_end_time=request.POST['est_end_time'], ride_creator=currentUser)
        return redirect('/bike/myrides')

def deleteuser(request, id):
    userToDelete = User.objects.filter(id=request.session['user'])
    if len(userToDelete) != 0:
        userToDelete[0].delete()
    return redirect('/')

def deleteride(request, id):
    rideToDelete = Ride.objects.filter(id=id)
    if len(rideToDelete) != 0:
        rideToDelete[0].delete()
    return redirect('/myaccount')