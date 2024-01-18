import uuid
from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=20, null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)
    quantity = models.IntegerField()
    fee = models.FloatField()
    
    def __str__(self):
        return str(self.title)


class Member(models.Model): 
    member_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    debt = models.FloatField()

    def __str__(self):
        return str(self.name)
    
class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)