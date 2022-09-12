from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Author, Book
from django.views import generic

class HomePage(generic.ListView):
    template_name = 'pracice/home.html'

    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'pracice/detail.html'


def add_book(request):
    if request.method == "POST":
        book_title = request.POST['book_title']
        author = request.POST['author']
        genre = request.POST['genre']
        language = request.POST['language']

        books = Book.objects.create(book_title=book_title, author=author, genre=genre, language=language)
        books.save()
        alert = True
        return render(request, 'pracice/add_book.html', {'alert': alert})
    return render(request, 'pracice/add_book.html')

"""
def detail(request,book_id):
    #book = get_object_or_404(Book, pk=book_id)
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book is not present in the library")
    
    return render(request, 'pracice/detail.html', {'book': book})
"""