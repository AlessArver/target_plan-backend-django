from django.urls import path
from django.urls.conf import include

from users.views import ListUsers, DetailUser

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/users/', ListUsers.as_view()),
    path('api/users/<int:pk>/', DetailUser.as_view()),
]