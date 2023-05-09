from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
     path('BookView/', BookView.as_view()) ,
     path('BookView/<int:id>', BookView.as_view())  


]