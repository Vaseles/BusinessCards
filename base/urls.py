from django.urls import path
from .views import auth, index, admin

app_name = 'base'

urlpatterns = [
    # auth
    path('sign-in', auth.sign_in, name='sign_in'),
    path('sign-out', auth.sign_out, name='sign_out'),
    
    path('', index.index, name='index'), 
    path('companies/<str:slug>', index.show_company, name='show_company'),
    
    # user and admin
    path('settings', index.settings, name='settings'),
    path('companies/<str:slug>/delete-company', index.delete_company, name='delete_company'),
    path('companies/<str:slug>/constructor', index.constructor, name='constructor'),
    path('companies/<str:slug>/update-info', index.add_more_fields, name='add_more_fields'),
    path('companies/<str:slug>/social-medias', index.social_medias, name='social_medias'),
    
    # admin  
    path('user/<str:username>/delete-user', admin.delete_user, name='delete_user'),
    path('create-card', admin.create_card, name='create_card'),
]
