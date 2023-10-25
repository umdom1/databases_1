from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_page(request, pub_date):
    url = request.get_full_path()
    if url == '/books/':
        page_obj = Book.objects.all()
    else:
        page_obj = Book.objects.filter(pub_date=pub_date)
    context = {'page_obj': page_obj}
    return render(request, 'books/books_page.html', context)

