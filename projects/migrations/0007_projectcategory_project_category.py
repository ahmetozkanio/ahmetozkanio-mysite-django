# Generated by Django 4.1.2 on 2022-10-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_rename_projectmodel_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(null=True, to='projects.projectcategory'),
        ),
    ]