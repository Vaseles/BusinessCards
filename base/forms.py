from django.forms import ModelForm, CharField, TextInput, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CompanySocialMedia, Company


class CompanySocialMediaForm(ModelForm):
   class Meta:
      model = CompanySocialMedia
      fields = '__all__'
   
class CreateUserForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
    password1 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': ' Password'}))
    password2 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': 'Repeat your password'}))
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UpdateUserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']
  
# Search Forms    
class UserSearchForm(Form):
   query = CharField(
      widget=TextInput(attrs={'placeholder': 'User search'}),
      required=False
      )


class CompanySearchForm(Form):
   query = CharField(
      widget=TextInput(attrs={'placeholder': 'Card search'}),
      required=False
      )

class CompanyUpdateForm(ModelForm):
   class Meta:
      model = Company
      fields = ['name', 
                'title', 
                'number', 
                'email', 
                'location',
                'about',
                'link_on_video']