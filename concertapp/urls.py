from django.urls import path
from concertapp import views

app_name = 'concertapp'
urlpatterns = [
    # path('list', views.ConcertListview.as_view(), name='list'),
    path('list/', views.performance_list_view, name='list'),
    path('<str:category>/', views.CategoryListView.as_view(), name="category"),
    path('detail/<int:pk>', views.PerformanceDetailView.as_view(), name="detail"),
]
