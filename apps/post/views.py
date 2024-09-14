from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from apps.post.models import *
from apps.post.serializers import PostSerializer

class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostAPICreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 