from django.urls import path
from .views import BookListView, add_book, EditBookView, DeleteBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', EditBookView.as_view(), name='edit_book'),
    path('books/delete/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
]
