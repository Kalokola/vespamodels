from django.db import models
import uuid
# Create your models here.
class Detection(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=250)
    image       = models.ImageField(blank=True, null=True, upload_to='images/')

class Categorise(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=250)
    cate       = models.CharField(max_length=250)