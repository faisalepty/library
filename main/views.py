from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.

def Home(request):
    books = Book.objects.all()[:12]
    context = {'books': books, 'h': 'h'}
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        query = request.GET.get('q')
        bookSearchs = Book.objects.filter(title__icontains=query)[:7]
        filterdData = [bookSearch.title for bookSearch in bookSearchs]
        return JsonResponse({'filterdData': filterdData, 'h': 'h'})
    return render(request, 'main/home.html', context)

def BookDetails(request):
    books = Book.objects.all()
    context = {'books': books, 'br': 'br'}
    filterdData = [book for book in books]
    print(filterdData)
    return render(request, 'main/BookDetails.html', context)
       
