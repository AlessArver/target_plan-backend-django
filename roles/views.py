from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from roles.serializers import RoleSerializer
from roles.models import Role 

class ListRoles(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class DetailRole(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CreateRole(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer