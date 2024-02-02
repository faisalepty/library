import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, User

from .utils import CalculateFine

# Create your models here.
class Book(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    edition = models.CharField(max_length=100, blank=True, null=True)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField(null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)
    quantity = models.IntegerField()
    fee = models.FloatField()
    STATUS = [
        ('Issued', 'Issued'),
        ('On shelf', 'on shelf')
    ]
    status = models.CharField(max_length=15, choices=STATUS, default='On shelf')
    copy_ids = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.copy_ids:
            copyids = [uuid.uuid4() for _ in range(self.quantity)]
            self.copy_ids = ",".join(str(copyid) for copyid in copyids)
        super().save(*args, **kwargs)

class Member(models.Model): 
    member_id = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    GENDERS = [('male', 'male'),
                ('female', 'female')
        ]
    gender = models.CharField(max_length=10, choices=GENDERS, null=True)
    age = models.IntegerField(null=True)
    debt = models.FloatField(default=0.0)
    member_since = models.DateTimeField(auto_now_add=True)
    profile_img = models.ImageField(upload_to='image/profile_imgs', default='static/image/dummy1.png', null=True) 
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    national_id = models.CharField(max_length=8)
    email = models.CharField(max_length=200)


    def __str__(self):
        return str(self.first_name)
    
class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    STATUS = [('returned', 'returned'),
                ('pending', 'pending'),
                ('extended', 'extended')
                ]
    status = models.CharField(max_length=50, choices=STATUS)
    copyId = models.CharField(max_length=50)
    fine = models.FloatField()
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()

    def CheckReturnDate(self):
        currentDate = timezone.now()
        if currentDate > self.return_date:
            self.status = 'extended'
            self.fine = CalculateFine(currentDate, self.return_date)
            self.save()


