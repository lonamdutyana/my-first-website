# user_auth/views.py
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.
@login_required
def index(request):
    return render(request, "user_auth/index.html")
# use login decorater to validate user authentication.


def about(request):
    return render(request, "user_auth/about.html")


def contact(request):
    return render(request, "user_auth/contact.html")


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:login')
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('user_auth:login')
# user_auth/views.py
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the polls app or any other desired URL
            return redirect('user_auth:index')  # Assuming 'polls:index' is the URL name for the polls index view
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})


# Create your views here.
