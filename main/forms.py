from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import CloudinaryFileField
from .models import Book, Member, Transaction



class Newbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class Newmemberform(forms.ModelForm):
    profile_img = CloudinaryFileField(required=False)
    class Meta:
        model = Member
        fields = '__all__'

class Transactionform(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book', 'member', 'return_date', 'fine', 'status', 'copyId']

class NewLibrarianForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LibrarianUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']