from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Home Page')

def roomPage(request):
    return HttpResponse('Room Page')

def profilePage(request):
    return HttpResponse('Profile Page')