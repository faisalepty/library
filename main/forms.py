from django import forms
from .models import Book, Member



class Newbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class Newmemberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'