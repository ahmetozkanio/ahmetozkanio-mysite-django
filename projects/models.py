from django.db import models

# Create your models here.

class Project(models.Model):
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 128, unique = True)
    description = models.TextField(blank = True,null = True)
    github_url = models.URLField(blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to="projects/",default = "projects/default.png")
    avaliable = models.BooleanField(default =True)
    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_images', on_delete=models.CASCADE)
    project_images =  models.ImageField(upload_to="projects/images",default = "projects/default.png")
    def __str__(self):
        return self.project

class ProjectTool(models.Model):
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    tool_name = models.CharField(max_length = 128)
    tool_icon = models.ImageField(upload_to = "projects/tools")
    def __str__(self):
        return self.project.name