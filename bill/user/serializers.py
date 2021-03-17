from django.contrib.auth import get_user_model
from rest_framework import serializers


from user.models import UserProfile

User = get_user_model()


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'mobile', 'gender', 'username', 'password', 'email']
