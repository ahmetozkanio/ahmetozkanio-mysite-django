from django.db import models

# Create your models here.

class ProjectModel(models.Model):
    project_name = models.CharField()
    #project_

class ProjectImageModel(models.Model):
    project = models.ForeignKey(ProjectModel)
    project_images = models.ImageField()
