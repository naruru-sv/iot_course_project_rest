from rest_framework import serializers
from .models import File


# class UploadSerializer(serializers.Serializer):

#     class Meta:
#         fields = ['file_uploaded']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
