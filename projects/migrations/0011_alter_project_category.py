# Generated by Django 4.1.2 on 2022-10-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_remove_projecttool_tool_icon_alter_project_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('W', 'Web'), ('D', 'Desktop')], max_length=8),
        ),
    ]
