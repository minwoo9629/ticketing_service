from django.urls import path
from concertapp import views

app_name = 'concertapp'
urlpatterns = [
    # path('list', views.ConcertListview.as_view(), name='list'),
    path('list', views.concert_list_view, name='list'),
]
