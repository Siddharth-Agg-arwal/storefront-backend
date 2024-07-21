from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # read the type of product/item liked by user
    object_id = models.PositiveBigIntegerField() #reference ID to the object
    content_object = GenericForeignKey() #read actual object