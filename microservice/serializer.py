from rest_framework import serializers
from .models import UrlData

class urlserializer(serializers.ModelSerializer):
    class Meta :
        model = UrlData
        fields = ('url',)