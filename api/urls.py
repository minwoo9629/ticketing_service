from django.urls import path, include
from api import views

app_name = 'api'
urlpatterns = [
    path('<str:category>/', views.CategoryListView.as_view(), name="category"),
    # path('search/', views.SearchListView.as_view(), name="search"),
]