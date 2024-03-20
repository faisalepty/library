from django.test import TestCase
from django.utils import timezone
from main.models import Book, Member, Transaction
import uuid

class BookModelTest(TestCase):

    def test_book_str(self):
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
        self.assertEqual(str(book), 'Test Book')

    def test_copy_ids_created(self):
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
        self.assertEqual(len(book.copy_ids.split(',')), book.quantity)

class MemberModelTest(TestCase):

    def test_member_str(self):
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
        self.assertEqual(str(member), 'John')

class TransactionModelTest(TestCase):

    def test_transaction_check_return_date(self):
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
        transaction = Transaction.objects.create(
            book=book,
            member=member,
            status='pending',
            copyId='copy_id_1',
            fine=0.0,
            issue_date=str(timezone.now().isoformat())[0:10],
            return_date=str(timezone.now().isoformat())[0:10]
        )
        transaction.CheckReturnDate()
        self.assertEqual(transaction.status, 'pending')
