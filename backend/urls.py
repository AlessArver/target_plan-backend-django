from django.contrib import admin
from django.urls import path

from roles.urls import urlpatterns as rolesUrls
from users.urls import urlpatterns as usersUrls
from targets.urls import urlpatterns as targetsUrls

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += rolesUrls
urlpatterns += usersUrls
urlpatterns += targetsUrls