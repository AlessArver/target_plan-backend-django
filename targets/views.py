from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from targets.serializers import TargetSerializer
from targets.models import Target

class ListTargets(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TargetSerializer

    def get(self, request, format=None):
        return Response(list(Target.objects.filter(user_id=request.user.id).values()))

class DetailTarget(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

class CreateTarget(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Target.objects.all()
    serializer_class = TargetSerializer