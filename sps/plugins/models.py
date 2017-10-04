from django.db import models
from django.contrib.postgres.fields import HStoreField


class PluginType(models.Model):
    code = models.CharField('Код', max_length=32, unique=True, primary_key=True)
    name = models.CharField('Навзание', max_length=127)


# Create your models here.
class Plugin(models.Model):
    id = models.UUIDField('ID', primary_key=True)
    name = models.CharField('Навзание', max_length=127)
    description = models.TextField('Описание')
    type = models.ForeignKey(PluginType, on_delete=models.SET_NULL, blank=True, null=True)
    params = HStoreField('Параметры')