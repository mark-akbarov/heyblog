# Generated by Django 3.2 on 2022-02-03 08:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220202_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]