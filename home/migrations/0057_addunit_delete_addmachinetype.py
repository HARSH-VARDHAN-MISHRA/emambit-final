# Generated by Django 4.2.7 on 2024-02-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_delete_createorder_purchaseorder_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='AddMachineType',
        ),
    ]