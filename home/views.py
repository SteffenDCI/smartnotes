from django.shortcuts import render
from django.http import HttpResponse

# Function-based view
def home(request):
    return HttpResponse('HTTP response working')

