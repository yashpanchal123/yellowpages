from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Yellow

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class YellowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yellow
        fields = '__all__'
