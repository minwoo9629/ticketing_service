from django.contrib.auth.views import LogoutView
from django.urls import path
from accountapp import views

app_name = 'accountapp'

urlpatterns = [
    # path('create/', views.create, name="create"),
    path('create/', views.AccountCreateView.as_view(), name="create"),
    path('login/', views.AccountLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('info/<int:pk>', views.AccountInfoView.as_view(), name="info"),
    path('delete/<int:pk>', views.AccountDeleteView.as_view(), name="delete"),  
]
