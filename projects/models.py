from django.db import models

# Create your models here.

class ProjectModel(models.Model):
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 128, unique = True)
    description = models.TextField(blank = True,null = True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="projects/%Y/%m/%d/",default = "projects/default.png")
    avaliable = models.BooleanField(default =True)
    #project_

class ProjectImageModel(models.Model):
    project = models.ForeignKey(ProjectModel, null=True, on_delete=models.CASCADE)
    project_images =  models.ImageField(upload_to="projects/%Y/%m/%d/",default = "projects/default.png")
