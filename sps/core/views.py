from django.contrib.auth.models import Group
from rest_framework import viewsets
from .api import UserSerializer, GroupSerializer
from .models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def start_info(request, format=None):
    queryset = User.objects.get(pk = 1)
    serializer = UserSerializer(queryset)
    return Response(serializer.data)