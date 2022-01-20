from django.shortcuts import render
from api.models import Assignment
from api.serializers import AssignmentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class AssignmentViews(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
