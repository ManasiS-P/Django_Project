"""Project_two URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppTwo/', include('AppTwo.urls')),  # Include AppTwo URLs
    # Optional: Add a root URL that redirects to AppTwo
    # path('', include('AppTwo.urls')),
]