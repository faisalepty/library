from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils import timezone
from django.db.models import Q
from .models import Book, Member, Transaction
from .forms import Newbookform, Newmemberform, Transactionform


# Home view for displaying a list of books or members based on user's search query
def Home(request):
    # Fetch a limited number of books for the home page
    books = Book.objects.all()
    members = Member.objects.all()
    transactions = Transaction.objects.all()
    showcasebooks = books[:12]
    showcasemembers = members[:12]


    issuedCopies = transactions.filter(Q(status='pending') | Q(status='extended')).count
    extendedCopies = transactions.filter(status='extended').count
    totalCopies = 0
    for book in books:
        copyIds = len(book.copy_ids.split(','))
        totalCopies += copyIds
    context = {'showcasebooks': showcasebooks, 'showcasemembers': showcasemembers, 'h': 'h', 'books': books, 'members': members, 'totalcopies': totalCopies, 'issuedCopies': issuedCopies, 'extendedCopies': extendedCopies}


    query = request.GET.get('q')
    qType = request.GET.get('searchType')
    filterdData = []
    bookSearch = books
    if query:
        # Handle different search types (member, title, author)
        if qType == 'member':
            userSearch = members.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
            context = {'members': userSearch}
            return render(request, 'main/members.html', context)
        elif qType in ['title', 'author']:
            bookSearch = bookSearch.filter(Q(title__icontains=query) | Q(author__icontains=query))
            context = {'books': bookSearch, 'br': 'br'}
            return render(request, 'main/bookDetails.html', context)
        else:
            bookSearch = bookSearch.filter(Q(title__icontains=query) | Q(author__icontains=query))
            context = {'books': bookSearch, 'br': 'br'}
            return render(request, 'main/bookDetails.html', context)
    return render(request, 'main/home.html', context)

# Display details of all books
def BooksDetails(request):
    books = Book.objects.all()
    context = {'books': books, 'br': 'br'}
    filterdData = [book for book in books]
    print(filterdData)
    return render(request, 'main/bookDetails.html', context)

# Display details of a specific book and its transactions
def BookInfo(request, pk):
    book = Book.objects.get(book_id=pk)
    transactions = book.transaction_set.all()
    context = {'book': book, 'transactions': transactions, 'bi': 'bi'}
    return render(request, 'main/bookInfo.html', context)

# Handle book issuance process
def IssueBook(request):
    q = request.GET.get('q')
    r = request.GET.get('r')
    if r:
        members = Member.objects.filter(
            Q(first_name__icontains=r)| 
            Q(last_name__icontains=r)
        )
        membersData = [f'{member.first_name} {member.last_name}' for member in members]
        return JsonResponse({'members': membersData})
    if q: 
        books = Book.objects.filter(title__icontains=q)
        booksData = [book.title for book in books]
        return JsonResponse({'books': booksData})
    
    if request.method =='POST':
        # Process book issuance
        book_title = request.POST.get('book_title')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        return_date = request.POST.get('return_date')

        book = Book.objects.get(title=book_title)
        member = Member.objects.get(first_name=first_name, last_name=last_name)
        bookTransHist = book.transaction_set.filter(Q(status='pending') | Q(status='extended'))
        issued_ids = [bookTrHis.copyId for bookTrHis in bookTransHist]
        copyIds = book.copy_ids.split(',')
        
        while copyIds:
            copyId = copyIds.pop()
            if copyId not in issued_ids:
                break
        if book.quantity > 0:
            form = Transactionform({'book': book, 'member': member, 'return_date': return_date, 'copyId': copyId, 'fine': 0, 'status': 'pending' })

            if form.is_valid():
                book.quantity -= 1
                member.debt += book.fee
                member.save()
                book.save()
                form.save()
                return JsonResponse({'success': 'success'})
            else:
                return JsonResponse({'form validation error': form.errors})
        else:
            return JsonResponse({'error': 'all books issued'})
    return JsonResponse({'members': 'books'})

# Handle book return process
def bookReturn(request, pk):
    if request.method == 'POST':
        bookCopy = Transaction.objects.get(Q(copyId=pk) & Q(status='pending') | Q(status='extended'))
        amount_paid = int(request.POST.get('amountPaid'))
        bookCopy.status = 'returned'
        bookCopy.book.quantity += 1
        bookCopy.member.debt -= amount_paid
        bookCopy.return_date = timezone.now()

        bookCopy.save()
        return JsonResponse({'success': 'success'})

# Handle the addition of a new book
def AddNewBook(request):
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = Newbookform(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': 'Book successfully added'})
            else:
                return JsonResponse({'Error': form.errors})
        else:
            return JsonResponse({'Error': 'Error2'})

# Handle the editing of book information
def EditBookInfo(request, pk):
    book = Book.objects.get(book_id=pk)
   
    if request.method == 'POST':
        form = Newbookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'Book successfully updated'})
        else:
            return JsonResponse({'Error': form.errors})
    data = {'title': book.title, 'author': book.author, 'description': book.description, 'language': book.language, 'category': book.category, 'edition': book.edition, 'pages': book.pages, 'publisher': book.publisher, 'publish_date': book.publish_date, 'img_url': book.img_url, 'quantity': book.quantity, 'fee': book.fee, 'status': book.status}
    return JsonResponse({'data': data})

# Handle the deletion of a book
def DeleteBook(request, pk):
    csrf_token = get_token(request)
    
    if request.method == 'POST':
        book = Book.objects.get(book_id=pk)
        book.delete()
        return JsonResponse({'success': 'Book deleted successfully'})

    return JsonResponse({'csrf_token': csrf_token})

# Display details of all members
def MembersDetails(request):
    members = Member.objects.all()
    context = {'members': members, 'mr': 'mr'}
    return render(request, 'main/members.html', context)

# Display details of a specific member
def MemberInfo(request, pk):
    member = Member.objects.get(member_id=pk)
    context = {'member': member, 'mi': 'mi'}
    return render(request, 'main/memberInfo.html', context)

# Handle the addition of a new member
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

# Handle the editing of member information
def EditMemberInfo(request, pk):
    member = Member.objects.get(member_id=pk)
    if request.method == 'POST':
        form = Newmemberform(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'Member successfully updated'})
        else:
            return JsonResponse({'Error': 'Error1'})
    data = {'first_name': member.first_name, 'last_name': member.last_name, 'gender': member.gender, 'age': member.age, 'debt': member.debt, 'profile_img': member.profile_img.url, 'address': member.address, 'mobile_no': member.mobile_no, 'national_id': member.national_id, 'email': member.email}
    return JsonResponse({'data': data})

# Handle the deletion of a member
def DeleteMember(request, pk):
    csrf_token = get_token(request)
    
    if request.method == 'POST':
        member = Member.objects.get(member_id=pk)
        member.delete()
        return JsonResponse({'success': 'Member deleted successfully'})

    return JsonResponse({'csrf_token': csrf_token})
