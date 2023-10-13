from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Function-based view


def home(request):
    return render(request, 'home/welcome.html')
