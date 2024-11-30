from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm  # Assuming you have a form for Book
from .forms import ExampleForm


# Sign Up View
class SignUpView(CreateView):
    form_class = UserCreationForm  # type: ignore
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# View for listing all books (requires can_view_book permission)
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    query = request.GET.get('q')  # Getting the search query from the request
    # Securely querying the books using Django ORM to prevent SQL injection
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# View to create a new book (requires can_add_book permission)
@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Save the new book, automatically associating it with the logged-in user
            book = form.save(commit=False)
            book.user = request.user  # Associate the book with the current user
            book.save()
            return redirect('book_list')  # Redirect to the book list page after adding the book
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

# View to update an existing book (requires can_change_book permission)
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Save the updated book details
            return redirect('book_list')  # Redirect after updating the book
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

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

    def get_queryset(self):
        query = self.request.GET.get('q')
        # Ensure the query is sanitized and safely executed using the ORM
        if query:
            # Avoid SQL injection by using Django ORM filter with safe query
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ['title', 'author', 'publication_year']

    def form_valid(self, form):
        # Ensuring that the logged-in user is the one adding the book
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = ['title', 'author', 'publication_year']

    def form_valid(self, form):
        # Ensure the user has permission to change the book
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



