from __future__ import unicode_literals

from django.db import models
from ..login.models import User


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookManager(models.Manager):
    def create_book(self, title, author, review):
        errors = []
        author = Author.objects.get(name=author)
        if not title:
            errors.append("Title field cannot be blank")
        if not review:
            errors.append("Review field cannot be blank")
        if Book.objects.filter(title=title).filter(author=author):
            errors.append("A book by that author already exists")
        if errors:
            return {"errors":errors}
        else:
            book = Book(title=title, author=author)
            book.save()
            return {"book":book}

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

class ReviewManager(models.Manager):
    def add_review(self, review, rating, book_id, user_id):
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=user_id)
        Review.objects.create(content=review, rating=rating, book=book, user=user)



class Review(models.Model):
    content = models.TextField(max_length=1000)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, related_name="book_reviews")
    user = models.ForeignKey(User, related_name="user_reviews")

    objects = ReviewManager()
