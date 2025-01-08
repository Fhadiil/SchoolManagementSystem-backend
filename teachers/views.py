from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Subject
from .serializers import TeacherSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
