from random import randrange, choice
from string import ascii_letters

from .models import Company
from django.contrib.auth.models import User


# Checking Slug
def generate_slug(title):
   slug = '-'.join(title.lower().split(' '))
   
   products = Company.objects.filter(slug=slug)
   
   if (products.count() > 0):
      slug += str(randrange(10000))
      return slug 
   else:
      return slug 

# username generator
def username_generator():
   username = ''.join([choice(ascii_letters) for _ in range(10)])
   
   users = User.objects.filter(username=username)
   
   if (users.count() > 0):
      username += str(randrange(10000))
      return username
   else:
      return username

# password generator
def password_generator():
    return ''.join([choice(ascii_letters) for _ in range(20)])
