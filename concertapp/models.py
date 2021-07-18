from django.db import models
from django.db.models import constraints
from django.db.models.base import Model

def poster_dirs_path(instance, filename):
    return 'poster/{}/{}'.format(instance.category, filename)

# 공연 모델
class Performance(models.Model):
    CATEGORY_CHOICES = [
        ('concert', '콘서트'),
        ('musical', '뮤지컬'),
        ('classic', '클래식'),
    ]
    title = models.CharField(max_length=100, verbose_name='공연 이름')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    poster = models.ImageField(upload_to=poster_dirs_path, null=True)

    def __str__(self):
        return self.title


# 공연장 모델
class ConcertHall(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# 공연장 좌석 모델
class Seat(models.Model):
    concert_hall = models.ForeignKey(ConcertHall, on_delete=models.CASCADE, related_name="seats")
    seat_type = models.CharField(max_length=10, verbose_name='좌석 등급')
    seat_number = models.IntegerField()
    reservation = models.BooleanField(default=False)


class Schedule(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name='schedule')
    concert_hall = models.ForeignKey(ConcertHall, on_delete=models.CASCADE, related_name='schedule')
    start_dt = models.DateTimeField(verbose_name='공연 시작 시간')
    end_dt = models.DateTimeField(verbose_name='공연 종료 시간')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['concert_hall', 'start_dt', 'end_dt'], name="place revervation time")
        ]