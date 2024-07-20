from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# request handler
# takes request and gives response

def say_hi(request):
    #pull data from db
    #transform
    #send email
    x = 1
    y = 2
    return render(request, 'helo.html')