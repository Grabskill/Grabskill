from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_id = models.EmailField(max_length=200)
    #genre = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.book_title