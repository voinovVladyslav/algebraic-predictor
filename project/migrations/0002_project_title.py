# Generated by Django 4.2 on 2023-04-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]