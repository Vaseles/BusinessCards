from django.forms import ModelForm, CharField, TextInput, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CompanySocialMedia, Company


class CreateNewCard(ModelForm):
    name_en = CharField(required=True)
    name_ru = CharField(required=True)
    name_kk = CharField(required=True)

    class Meta:
        model = Company
        fields = ('name_en', 'name_ru', 'name_kk', )
   
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

class CompanyUpdateForm(ModelForm):
    name_en = CharField(required=True)
    name_ru = CharField(required=True)
    name_kk = CharField(required=True)

    class Meta:
        model = Company
        fields = (
            'name_ru', 'name_kk', 'name_en',
            'title_ru', 'title_kk', 'title_en',
            'number',
            'email',
            'ava',
            'location_ru', 'location_kk', 'location_en',
            'about_ru', 'about_kk', 'about_en',
            'link_on_video'
        )

class CompanySocialMediaForm(ModelForm):
   class Meta:
      model = CompanySocialMedia
      fields = (
          'facebook','instagram', 'youtube', 'vk',
          'telegram', 'twitter', 'discord',
          'tiktok',
          'twitch', 'viber','skype',
          'pinterest', 'tumbler',
          'snapChat', 'whatsapp', 'linkedin',
          'soundCloud', 'spotify',
          'quora',  'github', 'sinaweibo',
          'their_website1', 'their_website2', 'their_website3',
          'yandex_taxi', 'yandex_cards', 'google_cards'
      )