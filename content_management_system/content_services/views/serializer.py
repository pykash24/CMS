
from rest_framework import serializers
from ..models import *

class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        fields = '__all__'


