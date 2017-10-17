from .models import User
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'groups', 'alias', 'first_name', 'last_name', 'middle_name', 'date_joined', 'avatar',
                  'vk_user_id', 'telegram_id')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')