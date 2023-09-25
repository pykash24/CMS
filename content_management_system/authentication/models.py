from django.db import models

""" 
    User Details Model
"""
class UserDetails(models.Model):
    user_id =models.CharField(unique=True,max_length=256, null=False)
    email =models.CharField(max_length=256, null=False)
    password =models.CharField(max_length=256, null=False)
    fullname =models.CharField(max_length=256, null=False)
    user_role =models.CharField(max_length=256, null=False)
    phone =models.IntegerField(max_length=256, null=False)
    address =models.CharField(max_length=256, null=True)
    city =models.CharField(max_length=256, null=True)
    state =models.CharField(max_length=256, null=True)
    country =models.CharField(max_length=256, null=True)
    pincode =models.IntegerField(max_length=256, null=False)
    is_deleted =models.IntegerField(max_length=256,default=False)
    created_datetime = models.DateTimeField(max_length=256, null=True)
    modified_datetime = models.DateTimeField(max_length=256, null=True)

    class Meta:
        db_table = "user_details"

""""

    User Content Models
    
"""

class ContentDetails(models.Model):
    content_id =models.CharField(unique=True,max_length=256, null=False)
    creator_id =models.CharField(UserDetails,on_delete=models.CASCADE,to_field='user_id')
    title =models.CharField(max_length=256, null=False)
    body =models.CharField(max_length=256, null=False)
    summary =models.CharField(max_length=256, null=False)
    document =models.CharField(max_length=256, null=False)
    categories =models.CharField(max_length=256, null=False)
    delete_by =models.CharField(max_length=256, null=True)
    is_deleted =models.IntegerField(max_length=256, default=False)
    created_datetime = models.DateTimeField(max_length=256, null=True)
    modified_datetime = models.DateTimeField(max_length=256, null=True)
    deleted_datetime = models.DateTimeField(max_length=256, null=True)

    class Meta:
        db_table = "content_details"