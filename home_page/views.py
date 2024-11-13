from django.shortcuts import render
from requests import request


def home(request):

    return render(request, 'index.html')

def about(request):

    return render(request,'users.html')
