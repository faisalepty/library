from django.contrib import admin
from .models import Book, Member, Transaction

# Register your models here.

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Transaction)
