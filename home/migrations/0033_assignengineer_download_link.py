# Generated by Django 4.2.7 on 2024-02-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_projectimage_projectcompletion'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignengineer',
            name='download_link',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
