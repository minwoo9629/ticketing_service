from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from concertapp.views import concert_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', concert_list_view, name='home'),
    path('concerts/', include('concertapp.urls')),
    path('accounts/', include('accountapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
