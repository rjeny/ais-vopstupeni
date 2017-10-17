from .models import Test
from rest_framework import serializers


class TestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'event', 'open_date', 'close_date', 'description', 'instructions', 'template', 'random_questions', 'plugin')
