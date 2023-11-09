from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm
from django.http import HttpResponse

# auth
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User Does Not Exist')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'User Name or Password Does Not Exist')
            
            
    context = {}
    return render(request,'base/auth/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')
    
# pages with crud operations
def homePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request, 'base/home.html',context)

def roomPage(request,pk):
    rooms = Room.objects.get(id=pk)
    context = {'room':rooms}
    return render(request, 'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed to update')
    
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed to delete')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request,'base/delete.html',context)
        
# profile poge
def profilePage(request):
    context = {}
    return render(request,'base/profilePage.html',context)