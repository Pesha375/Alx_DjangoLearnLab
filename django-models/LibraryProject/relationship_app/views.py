from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from.models import Book, Library, Author
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
   
def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name ='relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['library'] = library
return context  # type: ignore
     
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('library_list')
    else:
        form = UserCreationForm()
    return render(request,'relationship_app/register.html', {'form': form})  
   
