from imaplib import _Authenticator
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout



def login_view(request):
    if request.user.is_authenticated:
        return redirect('spent:index')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email  = email).first()
        if user and user.check_password(password):
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('spent:index')
        else:
            return render(request, 'auth/login.html', {'error': 'Incorrect Email or password', "email": email})
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('accounts:login_view')


