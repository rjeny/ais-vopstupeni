from django.db import models
from django.contrib.postgres.fields import HStoreField


# Create your models here.
class Test(models.Model):
    name = models.CharField('Название', max_length=255)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, blank=True, null=True)
    open_date = models.DateField('Дата открытия')
    close_date = models.DateField('Дата закрытия')
    description = models.TextField('Описание')
    instructions = models.TextField('Инструктаж', blank=True)
    template = models.BooleanField('Шаблон', default=False)
    random_questions = models.BooleanField('Сл. порядок вопросов', default=False)
    plugin = models.ForeignKey(
        'plugins.Plugin',
        limit_choices_to={'type__code': 'testing.test'},
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.TextField('Текст вопроса')
    sorting = models.IntegerField('Порядок вопросов')
    correct_answer = models.TextField('Правильный ответ', blank=True)
    max_mark = models.IntegerField('Максимальная оценка', default=10)
    plugin = models.ForeignKey(
        'plugins.Plugin',
        limit_choices_to={'type__code': 'testing.question'},
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    params = HStoreField('Параметры')
    
    
class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    answer = models.TextField('Ответ')
    start_timestamp = models.DateTimeField('Метка начала ответа', auto_now_add=True)
    last_timestamp = models.DateTimeField('Метка последнего обновления ответа', blank=True)
    finished = models.BooleanField('Ответ засчитан', default=False)
    params = HStoreField('Параметры')
    mark = models.IntegerField('Оценка')
    comment = models.TextField('Комментарий проверяющего')