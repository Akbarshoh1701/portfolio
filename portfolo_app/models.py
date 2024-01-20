from django.db import models

# Create your models here.

class About(models.Model):
    about_info = models.CharField(max_length=255)
    name_feld = models.CharField(max_length=255)
    name_filt_custom = models.CharField(max_length=255)
    birthday = models.DateField()


