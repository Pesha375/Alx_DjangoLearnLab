from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import login
from.models import Book, Library, Author
from.forms import BookForm
from django.contrib.auth.forms import UserCreationForm


# List Books with Search
def list_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Library Detail View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = self.get_object()
        return context


# User Registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.userprofile.role = 'Member'
            user.userprofile.save()
            login(request, user)
            return redirect(get_role_redirect(user))
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Add Book
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
