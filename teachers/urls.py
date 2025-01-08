from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
