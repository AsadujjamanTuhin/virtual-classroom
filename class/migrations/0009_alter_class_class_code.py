# Generated by Django 4.1 on 2022-08-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0008_alter_class_class_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_code',
            field=models.CharField(default='R97I5DYc', max_length=120),
        ),
    ]
