from asyncio.windows_events import NULL
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
    EventData = []
    for ride in Ride.objects.all():
        EventData.append({
                        'start': ride.dateofride,
                        'end': ride.dateofride,
                        'name': ride.ridetitle,
                        'distance': ride.distance,
                        'skill_level': ride.skill,
                        'url': '/bike/joinride/'+str(ride.id),
                        })                    
    print(EventData)
    context = {
        'user': user,
        'rides': Ride.objects.all(),
        "EventData": EventData,
    }
    return render(request, 'index.html', context)

def grouprides(request):
    user = User.objects.get(id=request.session['user'])
    context = {
        'user': user,
        'rides': Ride.objects.all(),
    }
    return render(request, 'grouprides.html', context)



def joinride(request, id):
    selected_ride = Ride.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])
    # Ride.rides_joined.add(user)
    context = {
        'user': user,
        'ride': selected_ride,
    }
    return render(request, 'groupridedate.html', context)

def myrides(request):
    user = User.objects.get(id=request.session['user'])
    context = {
        'user': user,
        'rides': Ride.objects.all(),
    }
    
    return render(request, 'myrides.html', context)

def location(request, id, startingpoint):
    ride = Ride.objects.get(id=id)
    startpoint = Ride.objects.get(startingpoint=startingpoint)
    print(startingpoint)
    url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

    querystring = {"address":startpoint}

    headers = {
        'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
        'x-rapidapi-key': "7acc907995msh096f900a346c1a8p12357ejsnad80b79afcfd"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return redirect('/bike/grouprides')

def join(request, id):
    myride = Ride.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])
    myride.rides_joined.add(user)
    myride.users_joined.add(user)
    return redirect('/bike/myrides')

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
        select_date = request.POST['date']
        context= {
            'select_date': select_date, 
        }
    else:
        return redirect('/bike')
        
    return render(request, 'createride.html', context)

def createride(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        if request.FILES:
            uploaded_route = request.FILES['routefile']
            print(uploaded_route.name)
            print(uploaded_route.size)
            fs = FileSystemStorage()
            fs.save(uploaded_route.name, uploaded_route)
        else:
            uploaded_route = None
        currentUser = User.objects.get(id=request.session['user'])
        newRide = Ride.objects.create(ridetitle=request.POST['ridetitle'], startingpoint= request.POST['startingpoint'], routefile= uploaded_route, distance=request.POST['distance'], dateofride=request.POST['dateofride'], skill=request.POST['skill'], desc=request.POST['desc'], ride_start_time=request.POST['ride_start_time'], est_end_time=request.POST['est_end_time'], ride_creator=currentUser)
        return redirect('/bike/myrides')

def deleteuser(request, id):
    userToDelete = User.objects.filter(id=request.session['user'])
    if len(userToDelete) != 0:
        userToDelete[0].delete()
    return redirect('/')

def deleteride(request, id, userid):
    rideToDelete = Ride.objects.filter(id=id)
    if len(rideToDelete) != 0:
        rideToDelete[0].delete()
    return redirect(f'/bike/myaccount/' +str(userid))

def edituser(request, id):
    user = User.objects.get(id=request.session['user'])
    errors = User.objects.user_edit_validator(request.POST, user)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/bike/myaccount/' +str(id))
    else:
        updateuser = User.objects.get(id=id)
        updateuser.fName = request.POST['fName']
        updateuser.lName = request.POST['lName']
        updateuser.email = request.POST['email']
        updateuser.skill = request.POST['skill']
        updateuser.preferred_ride_distance = request.POST['preferred_ride_distance']
        updateuser.save()
        return redirect(f'/bike/myaccount/' + str(id) )