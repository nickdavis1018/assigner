from api.models import Assignment
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User, Group

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id", "task", "assignee", "notes", "completed"]

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
       model = Group
       fields = ['url', 'name']