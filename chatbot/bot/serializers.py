# serializers.py

from rest_framework import serializers
from .models import StringInput

class StringInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringInput
        fields = ('promt', 'context')
