from django.db import models
from django.contrib.auth import get_user_model
from concertapp.models import Schedule, Seat
from django.db.models.signals import post_save
from django.dispatch import receiver

class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='reservation', null=True ,blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['schedule','seat'], name="not same reservation")
        ]    
    @property
    def reserved(self):
        if self.user is None:
            return False

    @receiver(post_save, sender=Schedule)
    def create_reservation(sender, instance, created, **kwargs):
        if created:
            print(instance)
            for seat in instance.concert_hall.seats.all():
                reservation = Reservation(schedule=instance, seat=seat)
                reservation.save()