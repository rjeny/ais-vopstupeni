from rest_framework import viewsets
from .api import TestsSerializer
from rest_framework import permissions
from .models import Test


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Test.objects.all()
    serializer_class = TestsSerializer
    permission_classes = (permissions.IsAuthenticated,)