from django.db import models

# Create your models here.
class GetImage(models.Model):
    img = models.ImageField(upload_to="")