from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.models import Assignment
from api.serializers import AssignmentSerializer, UserSerializer, GroupSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class AssignmentViews(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)