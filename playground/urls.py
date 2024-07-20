from django.urls import path
from . import views


#url conf aka url configuration module
urlpatterns = [
    path('hello/', views.say_hi)
]