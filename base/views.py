from django.shortcuts import render

rooms = [
    {
        'id':1,'name':'Lean Python'
    },
    {
        'id':2,'name':'Lean Flutter'
    },
    {
        'id':3,'name':'Lean SQL'
    },
]

def homePage(request):
    return render(request, 'home.html')

def roomPage(request):
    return render(request, 'room.html')

def profilePage(request):
    return render(request, 'profile.html')