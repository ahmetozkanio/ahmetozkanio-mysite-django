# Generated by Django 4.1.2 on 2022-10-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_accountmodel_userimagesmodel_delete_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
