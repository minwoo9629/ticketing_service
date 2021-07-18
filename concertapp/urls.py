from django.urls import path
from concertapp import views

app_name = 'concertapp'
urlpatterns = [
    # path('list', views.ConcertListview.as_view(), name='list'),
    path('list/', views.performance_list_view, name='list'),
    path('concert/', views.concert_list_view, name="conert"),
    path('detail/<int:pk>', views.PerformanceDetailView.as_view(), name="detail")
]
