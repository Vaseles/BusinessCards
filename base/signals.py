from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect

@receiver(user_logged_in)
def handle_user_logged_in(sender, user, request, **kwargs):
    if user.is_superuser:
        return redirect('/')
    
    if not request.session.get('first_login', False):
        return redirect('base:index')
    
    request.session['first_login'] = True
    return redirect('base:settings')