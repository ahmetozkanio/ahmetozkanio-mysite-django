# Generated by Django 4.1.2 on 2022-10-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_project_category_delete_projectcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttool',
            name='tool_icon',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='projects/default.png', null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_tr',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
    ]
