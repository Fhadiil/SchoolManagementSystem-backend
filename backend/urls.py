from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/students/', include('students.urls')),
    path('api/classes/', include('classes.urls')),
    path('api/teachers/', include('teachers.urls')),
]

