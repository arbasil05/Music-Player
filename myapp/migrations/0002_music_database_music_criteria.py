# Generated by Django 4.2.6 on 2024-07-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music_database',
            name='Music_Criteria',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
