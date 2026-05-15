from django.views.generic import ListView, DetailView
from django.db.models import F

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'  
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get('q', '')

        books = Book.objects.all()

        if search:
            books = books.filter(title__icontains=search)

        return books


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_object(self):
        obj = super().get_object()

        Book.objects.filter(pk=obj.pk).update(views=F('views') + 1)

        return obj