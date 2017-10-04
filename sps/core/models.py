from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from .managers import UserManager


# Create your models here.
class City(models.Model):
    DISTRICTS = (
        ('СЗФО', 'CЗФО'),
        ('ЦФО', 'ЦФО'),
        ('ЮФО', 'ЮФО'),
        ('СКФО', 'СКФО'),
        ('ПФО', 'ПФО'),
        ('УФО', 'УФО'),
        ('СФО', 'СФО'),
        ('ДФО', 'ДФО'),
        ('ДРУГОЕ', 'ДРУГОЕ'),
    )
    
    class META:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    
    name = models.CharField('Название', max_length=127)
    district = models.CharField('Регион', choices=DISTRICTS, max_length=127)
        
    def __str__(self):
        return self.name


class University(models.Model):
    id = models.UUIDField('Идентификатор', primary_key=True, unique=True, editable=False)
    alias = models.CharField('Элиас', unique=True, max_length=63)
    full_name = models.TextField('Название полное')
    name = models.TextField('Название', max_length=255)
    abbr = models.CharField('Аббривиатура', max_length=63)
    leader = models.CharField('Ректор', max_length=255)
    site = models.URLField('Сайт')
    params = JSONField('Параметрыв JSONe')
    emails = JSONField('Emails')
    phones = JSONField('Phones')
    
    def __str__(self):
        return self.name


class StudentsOrganisation(models.Model):
    id = models.UUIDField('Идентификатор', primary_key=True, editable=False)
    alias = models.CharField('Элиас', unique=True, max_length=63)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField('Название организации', max_length=255)
    site = models.URLField('Сайт организации')
    emails = JSONField('Emails')
    phones = JSONField('Phones')
    leader = JSONField('Ректор')
    
    def __str__(self):
        return self.university.__str__() + ' | ' + self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    alias = models.CharField('Ник', max_length=30, blank=True)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30, blank=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField('Активный', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    vk_user_id = models.CharField('Идентификатор vk', max_length=64, unique=True,  null=True)
    telegram_id = models.CharField('Идентификатор telegram',max_length=63,  unique=True,  null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField('Работничек', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
            """
            Returns the first_name plus the last_name, with a space in between.
            """
            full_name = '%s %s %s' % (self.first_name, self.last_name, self.last_name)
            return full_name.strip()

    def get_short_name(self):
            """
            Returns the short name for the user.
            """
            return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
            """
            Sends an email to this User.
            """
            send_mail(subject, message, from_email, [self.email], **kwargs)
            

class Notification(models.Model):
    TYPES = (
        ('success', 'success'),
        ('warning', 'warning'),
        ('fail', 'fail'),
    )
    
    user = models.ForeignKey(User)
    type = models.CharField('Тип сообщения', default='warning', choices=TYPES, max_length=63)
    text = models.TextField('Текст сообщения')
    timestamp = models.DateTimeField('Время создания', auto_now_add=True)
    unread = models.BooleanField('Непрочитано', default=True)