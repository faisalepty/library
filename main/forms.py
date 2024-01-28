from django import forms
from .models import Book, Member, Transaction



class Newbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class Newmemberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class Transactionform(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book', 'member', 'return_date', 'fine', 'status', 'copyId']