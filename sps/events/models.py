from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import Group


class Placement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Навзание', max_length=255)
    geo_yandex = models.CharField('GEO point yandex', max_length=127)
    geo_google = models.CharField('GEO point google', max_length=127)


# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=255)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата конца')


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    time_period = models.IntegerField('Дробь времени (мин)', default=30)
    is_official = models.BooleanField('Официальное', default=False)


class Flow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Навзание', max_length=127)
    description = models.TextField('Описание')
    sorting = models.IntegerField('Сортировка')
    user_group = models.ForeignKey(Group)


class ScheduleEvent(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    responsible = models.ForeignKey('core.User', on_delete=models.SET_NULL, blank=True, null=True)
    tags = ArrayField(models.CharField('Тег', max_length=63, blank=True))
    description = models.TextField('Описание')
    start = models.DateTimeField('Начало мероприятия', blank=True)
    end = models.DateTimeField('Конец мероприятия', blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    link = models.URLField('Ссылка', blank=True)
    flows = models.ManyToManyField(Flow)


class Application(models.Model):
    SIZES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    event = models.ForeignKey(Event)
    user = models.ForeignKey('core.User')
    form = models.ForeignKey('testing.Test', on_delete=models.CASCADE)
    size = models.CharField('Размер одежды', max_length=8, choices=SIZES)