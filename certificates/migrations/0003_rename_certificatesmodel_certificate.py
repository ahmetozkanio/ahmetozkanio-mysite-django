# Generated by Django 4.1.2 on 2022-10-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_alter_certificatesmodel_company_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CertificatesModel',
            new_name='Certificate',
        ),
    ]
