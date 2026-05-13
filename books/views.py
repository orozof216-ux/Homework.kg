from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import F
from .models import Book


def book_list(request):
    search = request.GET.get('q', '')

    books = Book.objects.all()

    if search:
        books = books.filter(title__icontains=search)

    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {
        'page_obj': page_obj,
        'search': search
    })


def book_detail(request, pk):
    Book.objects.filter(pk=pk).update(views=F('views') + 1)

    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/book_detail.html', {
        'book': book
    })