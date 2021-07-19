from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from concertapp.views import performance_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', performance_list_view, name='home'),
    path('performance/', include('concertapp.urls')),
    path('accounts/', include('accountapp.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
