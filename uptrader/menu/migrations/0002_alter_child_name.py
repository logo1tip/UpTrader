# Generated by Django 4.1.5 on 2023-01-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
