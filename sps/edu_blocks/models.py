from django.db import models


# Create your models here.
class EduBlock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    authors = models.ManyToManyField('core.User')
    code = models.CharField('Код', max_length=32, blank=True)
    feed_back = models.ForeignKey('testing.Test', on_delete=models.SET_NULL, blank=True, null=True)


def edu_block_path(instance, filename):
    return '/edu_blocks/id_{0}/{1}'.format(instance.edu_block.id, filename)


class EduBlockLanding(models.Model):
    edu_block = models.OneToOneField(EduBlock, on_delete=models.CASCADE, primary_key=True)
    header_image = models.ImageField('Картинка в шапку', upload_to=edu_block_path)
    sub_header = models.TextField('Подзаголовок', blank=True)


class EduBlockLandingBlock(models.Model):
    landing = models.ForeignKey(EduBlockLanding, on_delete=models.CASCADE, blank=True)
    is_template = models.BooleanField('Шаблон', default=False)
    nav_name = models.CharField('Пункт меню', max_length=63)
    sorting = models.IntegerField('Порядок блоков')
    anchor = models.CharField('Якорь', max_length=31)
    header = models.TextField('Подзаголовок')
    html = models.TextField('Код блока')
    css = models.TextField('Стили блока')


class EduBlockVisitor(models.Model):
    edu_block = models.ForeignKey(EduBlock, on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)


class EduBlockFile(models.Model):
    edu_block = models.ForeignKey(EduBlock, on_delete=models.CASCADE)
    file = models.FileField('Файл', upload_to=edu_block_path)
    description = models.TextField('Описание')
    for_everyone = models.BooleanField('Доступен всем', default=False)
    for_visitors = models.BooleanField('Для посетивших', default=False)
    for_organisation = models.BooleanField('Для оргов', default=False)