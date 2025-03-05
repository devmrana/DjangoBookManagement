from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

# View all books
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# Add a new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

# Edit a book
class EditBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/edit_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')

# Delete a book
class DeleteBookView(DeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_url = reverse_lazy('book_list')
