from django.urls import path

from roles.views import ListRoles, DetailRole, CreateRole

urlpatterns = [
    path('roles/', ListRoles.as_view()),
    path('roles/create/', CreateRole.as_view()),
    path('roles/<str:pk>/', DetailRole.as_view()),
]