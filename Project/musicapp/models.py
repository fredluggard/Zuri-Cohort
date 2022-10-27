from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    songs = models.ForeignKey(Song, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Lyric(models.Model):
    content = models.CharField(max_length=100)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

