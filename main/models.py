import uuid
from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
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
    
    def __str__(self):
        return str(self.title)


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
    profile_img = models.ImageField(upload_to='image/profile_imgs', default='/home/fhadhul/Desktop/fhadhul/library/static/images/user_1177568.png', null=True) 
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    national_id = models.CharField(max_length=8)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.first_name)
    
class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)