from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nine(requst):
    return HttpResponse("welcome 2023")