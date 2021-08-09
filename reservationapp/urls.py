from django.urls import path
from reservationapp import views

app_name = 'reservationapp'
urlpatterns = [
    path('reserve/<int:pk>', views.reserve, name="reserve")
]
