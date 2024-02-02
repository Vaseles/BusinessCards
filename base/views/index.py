from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q

from ..models import Company, CompanySocialMedia
from ..forms import CompanyUpdateForm, CompanySocialMediaForm


# ! /company/:slug - show company card
def show_company(request, slug: str): 
   company = Company.objects.get(slug=slug)
   company_icons = CompanySocialMedia.objects.get(contact=company)
   url = ''
   
   if company.link_on_video != '' or None:
    url = company.link_on_video.split('/')
    url[2] = 'www.youtube.com/embed'
    url = '/'.join(url)

   context = {
      'company': company, 
      'icons': company_icons,
      'link_on_video': url,
   }
   return render(request, 'base/cards/view.html', context)

# ! / - admin panel
@login_required(login_url='base:sign_in')
def index(request):
    companies = Company.objects.filter(user=request.user)
    
    if request.user.is_superuser:
        companies = Company.objects.all()

    search_type = request.GET.get('search_type')
    search = request.GET.get('query')

    if search_type == 'CompanySearch':
        companies = Company.objects.filter(
            Q(user__username__icontains=search) |
            Q(name_en__icontains=search) |
            Q(name_ru__icontains=search) |
            Q(name_kk__icontains=search)
        ).order_by('-updated')

        if not request.user.is_superuser:
            companies = companies.filter(user=request.user)
    
    users = []
    
    if request.user.is_superuser:
        users = User.objects.all()

        if search_type == 'UserSearch':
            users = User.objects.filter(
                Q(username__icontains=search) |
                Q(email__icontains=search)
            )

    context = {
        'companies': companies,
        'users': users,
    }
    return render(request, 'base/index.html', context)

# ! /company/:slug/delete-company - delete a company
@login_required(login_url='base:sign_in')
def delete_company(request, slug: str):
    try:
        type = 'company'
        company = Company.objects.get(slug=slug)
        
        if request.user.is_superuser or request.user == company.user:
            if request.method == 'POST':
                company.delete()
                messages.success(request, f'{company.name} has been deleted')
                return redirect('/')
            
            return render(request, 'base/delete.html', {'user': company, 'type': type})
    except:
        messages.error(request, 'Company does not exist')
        return redirect('base:index')

# ! /settings - update information about
@login_required(login_url='base:sign_in')
def settings(request):
   try:
        user = User.objects.get(id=request.user.id)
       
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_confirmation = request.POST.get('password_confirmation')
                        
            if user.username != username:
                usernames = User.objects.filter(username=username)
                
                if len(usernames) == 0:
                    user.username = username
                else:
                    messages.error(request, 'Username already exists')
                    return redirect('base:settings')
            
            if user.email != email:
                emails = User.objects.filter(email=email)
                
                if len(emails) == 0:
                    user.email = email
                else:
                    messages.error(request, 'Email already exists')
                    return redirect('base:settings')
            
            
            if password != '' and password_confirmation != '':
                if password == password_confirmation:
                    if len(password) > 7:
                        if check_password(password, user.password) == False:
                            user.password = make_password(password)
                    else:
                        messages.error(request, 'Password must be at least 8 characters long')
                        return redirect('base:settings')
                else:
                    messages.error(request, 'Password != Password Confirmation')
                    return redirect('base:settings')
                
            user.save()
            
            return redirect('base:index')
            
        return render(request, 'base/settings.html')
   except:
        messages.error(request, 'Company does not exist')
        return redirect('base:index')

# ! /company/:slug/constructor - update(constructor)
@login_required(login_url='base:sign_in')  
def constructor(request, slug:str):
    company = Company.objects.get(slug=slug)
    
    if request.user == company.user or request.user.is_superuser:
        company_icons = CompanySocialMedia.objects.get(contact=company)
    
        if request.method == 'POST':
            background_color = request.POST.get('background_color')
            
            company.background_color = background_color
            company.color = request.POST.get('color')
            
            company.card_background_color = request.POST.get('card_background_color')
            company.card_border_radius = request.POST.get('card_border_radius')
            company.card_box_shadow = request.POST.get('card_box_shadow')
            company.card_border = request.POST.get('card_border')
            
            company.card_image_border_radius = request.POST.get('card_image_border_radius')
            company.card_image_width = request.POST.get('card_image_width')
            company.card_image_height = request.POST.get('card_image_height')
            
            company.card_title_font_size = request.POST.get('card_title_font_size')
            company.card_title_font_family = request.POST.get('card_title_font_family')
            if  request.POST.get('card_title_font_color'):
                company.card_title_font_color = request.POST.get('card_title_font_color')
                company.card_title_font_weight = request.POST.get('card_title_font_weight')
                
                company.card_button_background_color = request.POST.get('card_button_background_color')
                company.card_button_color = request.POST.get('card_button_color')
                company.card_button_border_radius = request.POST.get('card_button_border_radius')
                company.card_button_box_shadow = request.POST.get('card_button_box_shadow')
                
                company.card_button_background_color_hover = request.POST.get('card_button_background_color_hover')
                company.card_button_color_hover = request.POST.get('card_button_color_hover')
                company.card_button_border_radius_hover = request.POST.get('card_button_border_radius_hover')
                company.card_button_box_shadow_hover = request.POST.get('card_button_box_shadow_hover')
            
            if (request.POST.get('card_text_font_size')):
                company.card_text_font_size = request.POST.get('card_text_font_size')
            if request.POST.get('card_text_font_family'):
                company.card_text_font_family = request.POST.get('card_text_font_family')
            if request.POST.get('card_text_color'):
                company.card_text_color = request.POST.get('card_text_color')
            if request.POST.get('card_text_font_weight'):
                company.card_text_font_weight = request.POST.get('card_text_font_weight')
            if request.POST.get('card_text_box_shadow'):
                company.card_text_box_shadow = request.POST.get('card_text_box_shadow')
            if request.POST.get('card_text_border_bottom'):
                company.card_text_border_bottom = request.POST.get('card_text_border_bottom')
            if request.POST.get('card_text_border'):
                company.card_text_border = request.POST.get('card_text_border')
            
            card_label_font_size = request.POST.get('card_label_font_size')
            card_label_font_family = request.POST.get('card_label_font_family')
            card_label_color = request.POST.get('card_label_color')
            card_label_font_weight = request.POST.get('card_label_font_weight')
            
            if card_label_font_size:
                company.card_label_font_size = card_label_font_size
            
            if card_label_font_family:
                company.card_label_font_family = card_label_font_family
            
            if card_label_color:
                company.card_label_color = card_label_color
            
            if card_label_font_weight:
                company.card_label_font_weight = card_label_font_weight
            
            name = request.POST.get('name')
            if name:
                company.name = name
            
            ava = request.FILES.get('ava', None)
            if ava:
                company.ava = ava
            
            title = request.POST.get('title')
            if (title and company.title != title): company.title = title
            
            location = request.POST.get('location')
            if (location and company.location != location): company.location = location
            
            number = request.POST.get('number')
            if (number and company.number != number): company.number = number
            
            email = request.POST.get('email')
            if (email and company.email != email): company.email = email
            
            about = request.POST.get('about')
            if (about and company.about != about): company.about = about
            
            link_on_video = request.POST.get('link_on_video')
            if (link_on_video and company.link_on_video!= link_on_video): company.link_on_video = link_on_video

            card_icon_color = request.POST.get('card_icon_color')
            if card_icon_color:
                company.card_icon_color = card_icon_color

            font_icon_size = request.POST.get('font_icon_size')
            if font_icon_size:
                company.font_icon_size = font_icon_size

            card_icon_color_hover = request.POST.get('card_icon_color_hover')
            if card_icon_color_hover:
                company.card_icon_color_hover = card_icon_color_hover
            
            company.save()
        
        context = {
            'company': company,
            'icons': company_icons
        }
        return render(request, 'base/cards/constructor.html', context)

# ! /company/:slug/add-fields - update(constructor)
@login_required(login_url='base:sign_in')  
def add_more_fields(request, slug:str):
    type = 'add_more_fields'
    company = Company.objects.get(slug=slug)
    
    if company.user == request.user  or request.user.is_superuser:
        form = CompanyUpdateForm(instance=company)
        
        if request.method == 'POST':
            form = CompanyUpdateForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                form.save()
                return redirect('base:constructor', slug=slug)
        
        context = {
            'company': company, 
            'form': form,
            'type': type
        }    
        return render(request, 'base/cards/update_info.html', context)
    else:
        messages.error(request, 'You are not authorized to access this page')
        return redirect('/')
    
# ! /company/:slug/social-medias - update(constructor)
@login_required(login_url='base:sign_in')  
def social_medias(request, slug:str):
    type = 'social_medias'
    company = Company.objects.get(slug=slug)
    
    if request.user == company.user or request.user.is_superuser:
        company_icons = CompanySocialMedia.objects.get(contact=company)
        form = CompanySocialMediaForm(instance=company_icons)
        
        if request.method == 'POST':
            form = CompanySocialMediaForm(request.POST, instance=company_icons)
            if form.is_valid():
                form.save()
                return redirect('base:constructor', slug=slug)
        
        context = {
            'company': company, 
            'form': form,
            'type': type
        }    
        return render(request, 'base/cards/update_info.html', context)
    else:
        messages.error(request, 'You are not authorized to access this page')
        return redirect('/')