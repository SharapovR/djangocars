from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CarSerializer, CallbackSerializer
from .models import Cars, Callback, CarsShots

class CarsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CallbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer
    # permission_classes = [permissions.IsAuthenticated]