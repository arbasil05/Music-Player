# Generated by Django 4.2.6 on 2024-07-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Music_Name', models.CharField(max_length=100)),
                ('Music_Artist', models.CharField(max_length=100)),
                ('Music_Banner', models.ImageField(upload_to='Banner/')),
                ('Music_File', models.FileField(upload_to='Music/')),
            ],
        ),
    ]