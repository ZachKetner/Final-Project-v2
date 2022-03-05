from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('grouprides', views.grouprides),
    path('joinride/<int:id>', views.joinride),
    path('myrides', views.myrides),
    path('myaccount/<int:id>', views.myaccount),
    path('updateaccount/<int:id', views.updateaccount),
    path('gotocreate', views.gotocreate),
    path('createride', views.createride),
    path('join/<int:id>', views.join),
    path('deleteride/<int:id>/<int:userid>', views.deleteride),
    path('deleteuser/<int:id>', views.deleteuser),
    path('edituser/<int:id>', views.edituser),
    path('location/<int:id>/<str:startingpoint>', views.location)
]
