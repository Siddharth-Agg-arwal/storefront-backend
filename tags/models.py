from django.db import models
# from store.models import Product  #POOR IMPLEMENTATION
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)

#find out what tag applies to which object
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product) BAD IMPLEMENTATION
    product = models.ForeignKey(ContentType, on_delete=models.CASCADE) #allows generic relations 
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('product', 'object_id') # to find the product/other item in generic relation