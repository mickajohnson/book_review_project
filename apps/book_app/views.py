from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import *

def index(request):
    books = Book.objects.all().order_by('title')
    currentthree = Review.objects.all().order_by('-id')[:3]
    context = {
            "books":books,
            "currentthree":currentthree
    }
    return render(request, 'book_app/index.html', context)

def add(request):
    authors = Author.objects.all()
    context = {
            "authors":authors
    }
    return render(request, 'book_app/add.html', context)

def add_book(request):
    if "id" not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect(reverse('books:add'))
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        review = request.POST["review"]
        rating = request.POST["rating"]
        user_id = request.session["id"]
        book = Book.objects.create_book(title, author, review)
        if "errors" in book:
            for error in book['errors']:
                messages.error(request, error)
            return redirect(reverse('books:add'))
        Review.objects.add_review(review, rating, book['book'].id, user_id)
        return redirect(reverse('books:show_book', kwargs={'id':book['book'].id}))
    else:
        return redirect(reverse('books:add'))

def add_author(request):
    if "id" not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect(reverse('books:add'))
    if request.method == "POST":
        name = request.POST['author']
        if Author.objects.filter(name__iexact=name):
            messages.error(request, "Author already exists")
            return redirect(reverse('books:add'))
        Author.objects.create(name=name)
    return redirect(reverse('books:add'))


def show_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        redirect(reverse('books:index'))
    reviews = Review.objects.filter(book=book)
    print reviews
    context = {
            "book": book,
            "reviews": reviews
    }
    return render(request, 'book_app/book.html', context)

def add_review(request, id):
    if "id" not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect(reverse('books:show_book', kwargs={'id':id}))
    if request.method == "POST":
        review = request.POST["review"]
        rating = request.POST["rating"]
        user_id = request.session["id"]
        book_id = id
        if not review:
            messages.error(request, "Review field can't be empty!")
        else:
            Review.objects.add_review(review, rating, book_id, user_id)
    return redirect(reverse('books:show_book', kwargs={'id':id}))

def show_user(request, id):
    try:
        user = User.objects.get(id=id)
        books = Book.objects.filter(book_reviews__user=user)
    except:
        return redirect(reverse('books:index'))
    context = {
            "user":user,
            "books":books
    }
    return render(request, 'book_app/user.html', context)

def destroy(request, id, review_id):
    try:
        Review.objects.get(id=review_id).delete()
    except:
        return redirect(reverse('books:index'))
    return redirect(reverse('books:show_book', kwargs={'id':id}))


def logout(request):
    del request.session['id']
    del request.session['alias']
    return redirect(reverse('login:index'))
