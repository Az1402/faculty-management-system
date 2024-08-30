from django.shortcuts import render, redirect
from .models import Dean, Department, Announcement, Message, Complaint
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    deans = Dean.objects.all()
    departments = Department.objects.all()
    announcements = Announcement.objects.all()
    return render(request, 'home.html', {
        'deans': deans,
        'departments': departments,
        'announcements': announcements
    })

def send_message(request):
    # Logic for sending messages
    pass

def submit_complaint(request):
    # Logic for submitting complaints
    pass

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home or any other page after successful login
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after successful signup
            return redirect('home')  # Redirect to home or any other page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
