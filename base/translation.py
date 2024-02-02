from modeltranslation.translator import register, TranslationOptions
from .models import Company

@register(Company)
class CompanyTranslationOptions(TranslationOptions):
   fields = ('name', 'title', 'location', 'about', )
