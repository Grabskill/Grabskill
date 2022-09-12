from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.artist + ' launched ' + self.album_name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_name = models.CharField(max_length=100)