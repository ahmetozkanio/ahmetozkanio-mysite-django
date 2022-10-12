from django.contrib import admin

from projects.models import ProjectImageModel, ProjectModel, ProjectToolsModel

# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(ProjectImageModel)
admin.site.register(ProjectToolsModel)