from rest_framework import serializers
from .models import Language, columns


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = columns


