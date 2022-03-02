from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('grouprides', views.grouprides),
    path('joinride/<int:id>', views.joinride),
    path('myrides', views.myrides),
    path('myaccount/<int:id>', views.myaccount),
    path('updateaccount/<int:id', views.updateaccount),
]
