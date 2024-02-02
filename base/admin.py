from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Company, CompanySocialMedia

@admin.register(Company)
class CompanyAdmin(TranslationAdmin):
   list_display = ('slug', 'name', 'email', 'number', 'updated', 'created')
   prepopulated_fields = {'slug': ('name',)}
   
admin.site.register(CompanySocialMedia)