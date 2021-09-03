from django.urls import path
from reservationapp import views

app_name = 'reservationapp'
urlpatterns = [
    path('reserve/<int:pk>', views.reserve, name="reserve"),
    path('reserve/payment_approval', views.payment_approval, name="payment_approval"),
    path('ticket/', views.TiketListView.as_view(), name="ticket_list"),
]
