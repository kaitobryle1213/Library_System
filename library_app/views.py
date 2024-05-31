# library_app/views.py

from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect
from .forms import UserForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def home(request):
    return render(request, 'home.html')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})