from django.db import models
from authentication.models import *

""""

    User Content Models
    
"""
class ContentDetails(models.Model):
    content_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator_id =models.ForeignKey(UserDetails,on_delete=models.CASCADE,to_field='user_id')
    title =models.CharField(max_length=256, null=False)
    body =models.CharField(max_length=256, null=False)
    summary =models.CharField(max_length=256, null=False)
    document =models.CharField(max_length=256, null=False)
    categories =models.CharField(max_length=256, null=False)
    delete_by =models.CharField(max_length=256, null=True)
    is_deleted =models.IntegerField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    deleted_datetime = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = "content_details"
        