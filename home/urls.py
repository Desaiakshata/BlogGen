from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "blogHome"
urlpatterns = [
    path("<int:id>", BlogView.as_view(), name="edit" )
]