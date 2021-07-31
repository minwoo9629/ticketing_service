from django.db import models
from django.db.models import constraints
from django.db.models.base import Model
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


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
    ticket_open_dt = models.DateTimeField(verbose_name='티켓 예매 시작 일시', null=True)
    advertisement = models.BooleanField(default=False)
    start_day = models.DateField(verbose_name='전체 공연 일정 시작 일자', null=True)
    end_day = models.DateField(verbose_name='전체 공연 일정 종료 일자', null=True)

    def __str__(self):
        return self.title

    @property
    def reserve_available(self):
        return self.ticket_open_dt < timezone.now()

    @property
    def d_day(self):
        if not self.reserve_available:
            return self.ticket_open_dt.date() - timezone.now().date()

class Description(models.Model):
    performance = models.OneToOneField(Performance, on_delete=models.CASCADE, related_name='description')
    description = RichTextUploadingField(null=True, blank=True)

# 공연장 모델
class ConcertHall(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# 공연장 좌석 모델
class Seat(models.Model):
    concert_hall = models.ForeignKey(ConcertHall, on_delete=models.CASCADE, related_name="seats")
    floor = models.CharField(max_length=10, verbose_name="층 수", default='스탠딩')
    area = models.CharField(max_length=10, verbose_name='공연장 구역', null=True)
    row = models.IntegerField(verbose_name="오 와 열 중 열을 뜻함",null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
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

    @property
    def time(self):
        return self.end_dt - self.start_dt
