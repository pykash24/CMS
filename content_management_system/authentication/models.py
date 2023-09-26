from django.db import models
import uuid
""" 
    User Details Model
"""
class UserDetails(models.Model):
    user_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email =models.CharField(max_length=256, null=False,blank=False)
    password =models.CharField(max_length=256, null=False,blank=False)
    fullname =models.CharField(max_length=256, null=False,blank=False)
    user_role =models.CharField(max_length=256, null=False,blank=False)
    phone =models.IntegerField(null=False,blank=False)
    address =models.CharField(max_length=256, null=True,blank=True)
    city =models.CharField(max_length=256, null=True,blank=True)
    state =models.CharField(max_length=256, null=True,blank=True)
    country =models.CharField(max_length=256, null=True,blank=True)
    pincode =models.IntegerField(null=False,blank=True)
    is_deleted =models.IntegerField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_details"

