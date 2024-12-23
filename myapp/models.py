from django.db import models

class Music_Database(models.Model):
    Music_Name = models.CharField(max_length=100)
    Music_Artist = models.CharField(max_length=100)
    Music_Criteria = models.CharField(max_length=100,default=1)
    Music_Banner = models.ImageField(upload_to='Banner')
    Music_File = models.FileField(upload_to='Music')

    def __str__(self):
        return self.Music_Name

class Artist(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Artist',blank=True, null=True)

    def __str__(self):
        return self.Name
    
class Moods(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='moods/')

    def __str__(self):
        return self.Name
    
