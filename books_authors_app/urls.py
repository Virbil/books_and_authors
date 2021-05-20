from django.urls import path
from . import views

urlpatterns = [
    # START OF URLS FOR BOOKS
    path('', views.books),
    path('submit-book', views.submit_book),
    path('books/<int:book_id>', views.book_info, name="book_info"),
    path('books/add-author', views.add_author),
    # END OF URLS FOR BOOKS

    # START OF URLS FOR AUTHORS
    path('authors', views.authors),
    path('submit-author', views.submit_author),
    path('authors/<int:author_id>', views.author_info, name="author_info"),
    path('authors/add-book', views.add_book),
]