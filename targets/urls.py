from django.urls import path

from targets.views import ListTargets, DetailTarget, CreateTarget

urlpatterns = [
    path('targets/', ListTargets.as_view()),
    path('targets/create/', CreateTarget.as_view()),
    path('targets/<int:pk>/', DetailTarget.as_view()),
]