from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.hashers import make_password

from ..utils import generate_slug, password_generator, username_generator
from ..models import Company, CompanySocialMedia


@user_passes_test(lambda u: u.is_superuser)
def create_card(request):
    type = 'create'
    users = User.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = generate_slug(name)
        user = request.POST.get('user')
                
        if (user == 'create_new'):
            username = username_generator()
            password = password_generator()
            
            user = User.objects.create(
                username = username,
                password = make_password(password) 
            )
        
            company = Company.objects.create(
                name = name,
                slug = slug,
                user = user
            )
            
            company_icons = CompanySocialMedia.objects.create(
                contact = company
            )
            
            return render(request, 'base/cards/create_after.html', {
                'username': username,
                'password': password,
            } )
        else:
            company = Company.objects.create(
                name = name,
                slug = slug,
                user = User.objects.get(id=user)
            )
            
            company_icons = CompanySocialMedia.objects.create(
                contact = company
            )
                     
            messages.success(request, f'Card {company.name} created')
            return redirect('base:index')
        
    context = {
        'users': users,
        'type': type
    }
    return render(request, 'base/cards/create.html', context)
    
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, username):
    try:
        user = User.objects.get(username=username)
        
        if request.user.is_superuser:
            if request.method == 'POST':
                user.delete()
                messages.success(request, f'{user.username} has been deleted')
                return redirect('/')
            
            return render(request, 'base/delete.html', {'user': user, 'type': 'company'})
    except:
        messages.error(request, 'User does not exist')
        return redirect('base:index')