
from rest_framework import serializers
from ..models import *
from configurations import constants

class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        fields = '__all__'
        
class UpdateUserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        fields = ['title', 'body', 'document','summary','categories','is_deleted','creator_id','content_id']  

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.document = validated_data.get('document', instance.document)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance



