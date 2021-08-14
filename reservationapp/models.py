from django.db import models
from django.contrib.auth import get_user_model
from concertapp.models import Schedule, Seat
from uuid import uuid4

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='reservation', null=True ,blank=True)
    reserve_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    number = models.UUIDField(editable=False, unique=True, null=True, blank=True)




class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='ticket', null=True ,blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='ticket', null=True, blank=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='ticket', null=True, blank=True)
    reserve = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='ticket')

    def __str__(self):
        return f"{self.schedule} {self.seat}"