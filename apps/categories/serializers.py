from rest_framework import serializers
from apps.categories.models import *

class CategotySelializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = '__all__'