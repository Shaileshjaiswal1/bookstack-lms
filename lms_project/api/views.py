from rest_framework.response import Response
from rest_framework.decorators import api_view
from lms_app.models import AddBook
from .serializers import BookSerializers
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages

# @api_view(['GET'])
# def getdata(request):
#     books = AddBook.objects.all()
#     serializer = BookSerializers(books,many=True)
#     return Response(serializer.data)

def dashboard(request):
    books = AddBook.objects.all()
    serializer = BookSerializers(books, many=True)
    print(serializer)
    return render(request, 'admin/dashboard.html', {'books': serializer.data})

def add_book_view(request):
    if request.method == 'POST':
        serializer = BookSerializers(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'admin/add_book.html', {'success': True})
        else:
            return render(request, 'admin/add_book.html', {'errors': serializer.errors})
    
    return render(request, 'admin/add_book.html')

def edit_book_view(request, book_id):
    try:
        book = get_object_or_404(AddBook, id=book_id)
        if request.method == "POST":
            title = request.POST.get('title')
            author = request.POST.get('author')

            book.title = title
            book.author = author
            book.save()

            messages.success(request, 'Book updated successfully!')
            return redirect('edit_book', book_id=book.id)
        return render(request, 'admin/edit_book.html', {'book': book})
    except AddBook.DoesNotExist:
        raise Http404("Book not found")

def delete_book_view(request, delete_book):
    try:
        book = get_object_or_404(AddBook, id=delete_book)
        book.delete()
        return redirect('dashboard')
    except AddBook.DoesNotExist:
        raise Http404("Book not found")

# def view_book(request):
#     books = AddBook.objects.all()
#     serializer = BookSerializers(books, many=True)
#     return render(request, 'student/view_books.html', {'books': serializer.data})



