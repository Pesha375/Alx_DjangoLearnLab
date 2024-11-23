from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from.models import Book, Library, Author

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['library'] = library
        return context