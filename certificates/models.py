
from django.db import models

# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length= 256)
    company_name = models.CharField(max_length = 128)
    # company_icon = models.ImageField(upload_to = "certificate/icon",blank=True,null = True)
    certificate_image = models.ImageField(upload_to = "certificate/image",blank=True,null = True)
    certificate_url = models.URLField(blank = True,null = True)
    date = models.DateField()
    avaliable = models.BooleanField(default = True)
    def __str__(self):
        return self.name