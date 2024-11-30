from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import login
from .models import Book, Library, Author
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm

# List Books with Search (requires can_view_book permission)
@permission_required('relationship_app.can_view_book', raise_exception=True)
def list_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Library Detail View (no permissions needed for view)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = self.get_object()
        return context


# User Registration (Assigning role during user registration)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating UserProfile and assigning the default role
            user.userprofile.role = 'Member'  # Default role for new users
            user.userprofile.save()
            login(request, user)
            return redirect(get_role_redirect(user))  # Redirect based on role
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Redirect based on user role (helper function)
def get_role_redirect(user):
    if user.userprofile.role == 'Admin':
        return 'admin_view'  # Assuming 'admin_view' is the URL for the admin page
    return 'book_list'  # Default redirect to book list for non-admin users


# Admin View (restricted to users with is_admin function check)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Add Book (requires can_add_book permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


# Additional Helper function to check if the user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'


# Edit Book (requires can_change_book permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# Delete Book (requires can_delete_book permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})

