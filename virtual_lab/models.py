from django.db import models

# Create your models here.
class slideshow(models.Model):
    slideshow_img = models.ImageField(upload_to="pics")