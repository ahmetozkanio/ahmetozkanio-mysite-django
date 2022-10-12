# Generated by Django 4.1.2 on 2022-10-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificatesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('company_name', models.CharField(max_length=128)),
                ('company_icon', models.ImageField(upload_to='certificate/company')),
                ('certificate_image', models.ImageField(upload_to='certificate/image')),
                ('certificate_url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('avaliable', models.BooleanField(default=True)),
            ],
        ),
    ]