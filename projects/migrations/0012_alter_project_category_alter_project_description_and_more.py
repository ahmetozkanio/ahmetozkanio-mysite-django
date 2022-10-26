# Generated by Django 4.1.2 on 2022-10-26 18:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('mobile', 'Mobile'), ('web', 'Web'), ('desktop', 'Desktop')], max_length=8),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_tr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project_images',
            field=models.ImageField(blank=True, default='projects/default.png', null=True, upload_to='projects/images'),
        ),
        migrations.AlterField(
            model_name='projecttool',
            name='tool_name',
            field=models.CharField(blank=True, choices=[('flutter', 'Flutter'), ('android', 'Android'), ('ios', 'IOS'), ('figma', 'Figma'), ('adobexd', 'Adobe Xd'), ('django', 'Django'), ('djangorestapi', 'Django Rest Api'), ('firebase', 'Firebase')], max_length=16, null=True),
        ),
    ]