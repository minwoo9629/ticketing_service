from django.urls import path, include
from api import views

app_name = 'api'
urlpatterns = [
    path('<str:category>/', views.CategoryListView.as_view(), name="category"),
    path('reservation/remain/', views.RemainTicketCountView.as_view(), name="remain"),
    path('reservation/price/', views.GetTicketPrice.as_view(), name="price"),
]
