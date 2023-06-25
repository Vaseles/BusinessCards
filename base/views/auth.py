from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.models import User
from datetime import datetime
from ..forms import CreateUserForm, UpdateUserForm


def sign_in(request):
    page_type = 'Sign In'
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                if user.is_superuser:
                    return redirect('base:index')
                else:
                    if user.date_joined.strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d"):
                        return redirect('base:settings')
                    else:
                        return redirect('base:index')
            else:
                messages.error(request, 'Invalid username or password')
                
        except:
            messages.error(request, 'Invalid username')
    
    context = {
        'page_type': page_type,
    }
    return render(request, 'base/sign_in.html',context)

@login_required(login_url='base:sign_in')
def sign_out(request):
    logout(request)
    
    messages.success(request, 'Logged out successfully')
    return redirect('base:sign_in')