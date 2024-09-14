from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from apps.tasks.models import *
from apps.tasks.serializers import *

class TaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class TaskAPICreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer