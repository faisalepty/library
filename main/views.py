from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import Book
from .forms import Newbookform, Newmemberform

# Create your views here.

def Home(request):
    books = Book.objects.all()[:12]
    bookcount = Book.objects.all().count
    context = {'books': books, 'h': 'h', 'bookcount': bookcount}
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        query = request.GET.get('q')
        bookSearchs = Book.objects.filter(title__icontains=query)[:7]
        filterdData = [bookSearch.title for bookSearch in bookSearchs]
        return JsonResponse({'filterdData': filterdData, 'h': 'h'})
    return render(request, 'main/home.html', context)

def BooksDetails(request):
    books = Book.objects.all()
    context = {'books': books, 'br': 'br'}
    filterdData = [book for book in books]
    print(filterdData)
    return render(request, 'main/bookDetails.html', context)


def BookInfo(request, pk):
    book = Book.objects.get(title__icontains='the book thief')
    context = {'book': book}
    return render(request, 'main/bookInfo.html', context)


def AddNewBook(request):
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = Newbookform(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': 'Book successfuly added'})
            else:
                return JsonResponse({'Error': 'Error1'})
        else:
            return JsonResponse({'Error': 'Error2'})

def AddNewMember(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
        file = request.FILES.get("image")
        form = Newmemberform(request.POST, request.FILES)
        print(request.POST, file)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'success'})
        else:
            errors = dict(form.errors)
            return JsonResponse({'error': 'form validation error', 'errors': errors})
    else:
        return JsonResponse({'error': 'bad request'})

def EditBookInfo(request, pk):
    book = Book.objects.get(book_id=pk)
   
    if request.method == 'POST':
        print(request.POST)
        form = Newbookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'Book successfuly updated'})
        else:
            return JsonResponse({'Error': form.errors})
    data = {'title': book.title, 'author': book.author, 'description': book.description, 'language': book.language, 'category': book.category, 'edition': book.edition, 'pages': book.pages, 'publisher': book.publisher, 'publish_date': book.publish_date, 'img_url': book.img_url, 'quantity': book.quantity, 'fee': book.fee, 'status': book.status}
    return JsonResponse({'data': data})

def DeleteBook(request, pk):
    csrf_token = get_token(request)
    
    if request.method == 'POST':
        book = Book.objects.get(book_id=pk)
        book.delete()
        return JsonResponse({'success': 'Book deleted succesfully'})

    return JsonResponse({'csrf_token': csrf_token})


def EditMemberInfo(request, pk):
    member = Member.objects.get(member_id=pk)
    if request.method == 'POST':
        form = NewMemberform(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'member successfuly updated'})
        else:
            return JsonResponse({'Error': 'Error1'})
    data = {'first_name': first_name, 'last_name': last_name, 'gender': gender, 'age': age, 'debt': debt, 'profile_img': profile_img, 'address': address, 'mobile_no': mobile_no, 'national_id': national_id, 'email': email}
    return JsonResponse({'data': data})

def DeleteMember(request):
    csrf_token = get_token(request)
    
    if request.method == 'POST':
        member = Member.objects.get(member_id=pk)
        member.delete()
        return JsonResponse({'success': 'Member deleted succesfully'})

    return JsonResponse({'csrf_token': csrf_token})