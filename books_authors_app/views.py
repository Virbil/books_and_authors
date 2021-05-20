from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Start Methods for Book pages
def books(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "books.html", context)

def submit_book(request):
    if request.method == "POST":
        Book.objects.create(
            title = request.POST["title"],
            desc = request.POST["desc"]
        )        
        return redirect('/')
    else:
        return redirect('/')

def book_info(request, book_id):
    context = {
        "book_info": Book.objects.get(id=book_id),
        "authors": Author.objects.filter(books=Book.objects.get(id=book_id)),
        "other_authors": Author.objects.exclude(books=Book.objects.get(id=book_id))
    }
    return render(request, "book-info.html", context)

def add_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author'])
    # print(this_book.__dict__)
    # print(this_author.__dict__)
    this_author.books.add(this_book)
    return redirect('/')
# End Methods for Book pages

# Start Methods for Author pages
def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def submit_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"],
            notes = request.POST["notes"]
        )        
        return redirect('/authors')
    else:
        return redirect('/authors')

def author_info(request, author_id):
    book_by_auth = Author.objects.get(id=author_id).books.all()
    all_books = Book.objects.all()
    context = {
        "author_info": Author.objects.get(id=author_id),
        "books": book_by_auth,
        "other_books": all_books.difference(book_by_auth)
    }
    return render(request, "author-info.html", context)

def add_book(request):
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book = Book.objects.get(id=request.POST['book'])
    # print(this_book.__dict__)
    # print(this_author.__dict__)
    this_author.books.add(this_book)
    return redirect('/authors')
# End Methods for Author pages