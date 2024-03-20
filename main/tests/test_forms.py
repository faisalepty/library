from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from main.forms import Newbookform, Newmemberform, Transactionform, NewLibrarianForm, LibrarianUpdateForm
from cloudinary.forms import CloudinaryFileField
from main.models import Book, Member, Transaction


class TestForms(TestCase):
    def test_new_book_form(self):
        form = Newbookform(data={
            'title': 'Test Book',
            'author': 'Test Author',
            'description': 'Test Description',
            'language': 'English',
            'category': 'Test Category',
            'edition': 'First Edition',
            'pages': 200,
            'publisher': 'Test Publisher',
            'publish_date': '2023-01-01',
            'img_url': 'https://via.placeholder.com/300',
            'quantity': 10,
            'fee': 5.00,
            'status': 'On shelf'
        })
        self.assertTrue(form.is_valid())

    def test_new_member_form(self):
        form = Newmemberform(data={
            'first_name': 'Test',
            'last_name': 'Member',
            'gender': 'male',
            'age': 30,
            'debt': 0.00,
            'address': 'Test Address',
            'mobile_no': '1234567890',
            'national_id': 'ABCD1234',
            'email': 'test@example.com',
            'profile_img': None  # You can add a CloudinaryFileField value if needed
        })       
        self.assertTrue(form.is_valid())

    def test_transaction_form(self):
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            language='English',
            category='Test Category',
            edition='First',
            pages=200,
            publisher='Test Publisher',
            publish_date=timezone.now().date(),
            quantity=2,
            fee=10.0
        )
        member = Member.objects.create(
            first_name='John',
            last_name='Doe',
            gender='male',
            age=30,
            debt=0.0,
            address='Test Address',
            mobile_no='1234567890',
            national_id='12345678',
            email='test@example.com'
        )
        form = Transactionform(data={
            'book': book.id,
            'member': member.id,
            'return_date': '2023-02-01',
            'fine': 0.00,
            'status': 'pending',
            'copyId': 'TestCopyId'
        })
        print (form.errors)
        self.assertTrue(form.is_valid())

    def test_new_librarian_form(self):
        form = NewLibrarianForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        })
        self.assertTrue(form.is_valid())

    def test_librarian_update_form(self):
        user = User.objects.create(username='testuser', email='testuser@example.com')
        form = LibrarianUpdateForm(instance=user, data={
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        })
        self.assertTrue(form.is_valid())
