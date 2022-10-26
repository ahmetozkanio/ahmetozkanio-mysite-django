
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

PROJECT_CATEGORY = (
    ('mobile','Mobile'),
    ('web', 'Web'),
    ('desktop', 'Desktop'),
)
PROJECT_TOOLS = (
    ('flutter','Flutter'),
    ('android', 'Android'),
    ('java', 'Java'),
    ('ios', 'IOS'),
    ('figma', 'Figma'),
    ('adobexd', 'Adobe Xd'),
    ('django', 'Django'),
    ('djangorestapi', 'Django Rest Api'),
    ('firebase', 'Firebase'),
)

class Project(models.Model):
    name = models.CharField(max_length = 256, unique = True)
    description = RichTextField(blank = True,null = True)
    github_url = models.URLField(blank=True,null =True)
    date = models.DateField()
    category = models.CharField(max_length=8,choices=PROJECT_CATEGORY)
    image = models.ImageField(upload_to="projects/",default = "projects/default.png",null =True)
    avaliable = models.BooleanField(default =True,)
    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_images', on_delete=models.CASCADE)
    project_images =  models.ImageField(upload_to="projects/images",default = "projects/default.png",null=True,blank= True)
    def __str__(self):
        return self.project.name

class ProjectTool(models.Model):
    project = models.ForeignKey(Project,related_name='project_tools',on_delete = models.CASCADE)
    tool_name = models.CharField(max_length=16,choices=PROJECT_TOOLS,null=True,blank= True)
    def __str__(self):
        return self.project.name


