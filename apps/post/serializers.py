from rest_framework import serializers
from apps.post.models import * 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'