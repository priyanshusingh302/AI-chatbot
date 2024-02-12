from rest_framework import serializers
from .models import StringInput


class StringInputSerializer(serializers.ModelSerializer):
    context = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = StringInput
        fields = ('promt', 'context')
