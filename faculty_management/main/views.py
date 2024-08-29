from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from .models import Dean, Department, Announcement, Message, Complaint
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import Dean

def home(request):
    # if request.method=='POST':
    #     uname = request.POST.get('username')
    #     userobj = User.objects.get(id=id)
    #     Dean.objects.create(user=)
    #     Dean.save()
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



def login(request):
    # Logic for login view
    return render(request, 'login.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home or any other page after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    

def signup(request):
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
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')