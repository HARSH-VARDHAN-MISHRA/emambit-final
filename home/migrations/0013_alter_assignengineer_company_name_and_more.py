# Generated by Django 4.2.7 on 2024-02-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_assignengineer_engineer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignengineer',
            name='company_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='assignengineer',
            name='engineer_name',
            field=models.CharField(max_length=100),
        ),
    ]