from django.contrib.auth import logout
from django.shortcuts import redirect

class SuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_superuser:
            return self.get_response(request)
        else:
            logout(request)
            return redirect('base:sign_in')