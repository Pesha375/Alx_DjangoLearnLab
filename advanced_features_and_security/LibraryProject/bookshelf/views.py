from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Book

# Sign Up View
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# View for listing all books (requires can_view_book permission)
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# View to create a new book (requires can_add_book permission)
@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Handle form submission to add book (you would typically use a form here)
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        
        # Assuming 'user' is the logged-in user who is adding the book
        book = Book.objects.create(title=title, author=author, publication_year=publication_year, user=request.user)
        return redirect('book_list')  # Redirect to the book list page after adding the book
    
    return render(request, 'add_book.html')


# View to update an existing book (requires can_change_book permission)
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        # Handle form submission to update book
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')  # Redirect after updating the book
    
    return render(request, 'edit_book.html', {'book': book})


# View to delete a book (requires can_delete_book permission)
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect after deleting the book
    
    return render(request, 'delete_book.html', {'book': book})


# Class-based views for Book (listing, creating, updating, deleting)
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ['title', 'author', 'publication_year', 'user']

    def form_valid(self, form):
        # Ensuring that the logged-in user is the one adding the book
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = ['title', 'author', 'publication_year']

    def form_valid(self, form):
        # Ensuring that the user can only update if they have permission
        if not self.request.user.has_perm('bookshelf.can_change_book'):
            return redirect('book_list')  # Or raise a permission error
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('book_list')  # Redirect after deletion

    def dispatch(self, request, *args, **kwargs):
        # Check if the user has delete permission before proceeding
        if not request.user.has_perm('bookshelf.can_delete_book'):
            return redirect('book_list')  # Or raise a permission error
        return super().dispatch(request, *args, **kwargs)
