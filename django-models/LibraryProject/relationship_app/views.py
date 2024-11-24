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
     
def login_view(request):
    """
    Logs in a user with the provided credentials.
    """
    authentication_form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST' and authentication_form.is_valid():
        user = authentication_form.get_user()
        login(request, user)
        return redirect('library_list')
    return render(
        request, 'login.html', {'form': authentication_form}
    )

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form': form}) 

     
     
     