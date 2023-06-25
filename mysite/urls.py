from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', include('base.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('base.urls')),
)