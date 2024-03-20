from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Book, Member, Transaction

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_view(self):
        # Test login view with correct credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Should redirect to home upon successful login

        # Test login view with incorrect credentials
        response = self.client.post(reverse('login'), {'username': 'invalid', 'password': 'invalid'})
        self.assertEqual(response.status_code, 302)  # Should redirect back to login page

    def test_logout_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_home_view_authenticated(self):
        # Test home view when user is logged in
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Should return success

    def test_home_view_unauthenticated(self):
        # Test home view when user is not logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_books_details_view(self):
        # Test books details view
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('bookdetails'))
        self.assertEqual(response.status_code, 200)  # Should return success

    def test_book_info_view(self):
        # Test book info view
        self.client.login(username='testuser', password='password123')
        book = Book.objects.create(title='Test Book', author='Test Author', description='Test Description', language='English', category='Test Category', edition='First', pages=200, publisher='Test Publisher', publish_date='2022-01-01', quantity=1, fee=10.0)
        response = self.client.get(reverse('bookinfo', args=[book.book_id]))
        self.assertEqual(response.status_code, 200)  # Should return success

    def test_issue_book_view(self):
        # Test issue book view
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('issuebook'), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_add_new_book_view(self):
        # Test add new book view
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('addnewbook'), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_edit_book_info_view(self):
        # Test edit book info view
        self.client.login(username='testuser', password='password123')
        book = Book.objects.create(title='Test Book', author='Test Author', description='Test Description', language='English', category='Test Category', edition='First', pages=200, publisher='Test Publisher', publish_date='2022-01-01', quantity=1, fee=10.0)
        response = self.client.post(reverse('editbookinfo', args=[book.book_id]), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_delete_book_view(self):
        # Test delete book view
        self.client.login(username='testuser', password='password123')
        book = Book.objects.create(title='Test Book', author='Test Author', description='Test Description', language='English', category='Test Category', edition='First', pages=200, publisher='Test Publisher', publish_date='2022-01-01', quantity=1, fee=10.0)
        response = self.client.post(reverse('deletebook', args=[book.book_id]))  # Provide a valid book ID
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_members_details_view(self):
        # Test members details view
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('membersdetails'))
        self.assertEqual(response.status_code, 200)  # Should return success

    def test_member_info_view(self):
        # Test member info view
        self.client.login(username='testuser', password='password123')
        member = Member.objects.create(first_name='Test', last_name='Member', gender='male', age=30, debt=0.0, address='Test Address', mobile_no='1234567890', national_id='12345678', email='test@example.com')
        response = self.client.get(reverse('memberinfo', args=[member.member_id]))
        self.assertEqual(response.status_code, 200)  # Should return success

    def test_add_new_member_view(self):
        # Test add new member view
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('addnewmember'), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_edit_member_info_view(self):
        # Test edit member info view
        self.client.login(username='testuser', password='password123')
        member = Member.objects.create(first_name='Test', last_name='Member', gender='male', age=30, debt=0.0, address='Test Address', mobile_no='1234567890', national_id='12345678', email='test@example.com')
        response = self.client.post(reverse('editmemberinfo', args=[member.member_id]), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_delete_member_view(self):
       
        # Test delete member view
        self.client.login(username='testuser', password='password123')
        member = Member.objects.create(first_name='Test', last_name='Member', gender='male', age=30, debt=0.0, address='Test Address', mobile_no='1234567890', national_id='12345678', email='test@example.com')
        response = self.client.post(reverse('deletemember', args=[member.member_id]))  # Provide a valid member ID
        self.assertEqual(response.status_code, 200)  # Example, modify as needed

    def test_add_new_librarian_view(self):
        # Test add new librarian view
        self.client.login(username='admin', password='admin123')
        response = self.client.post(reverse('librarians'), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 302)  # Example, modify as needed

    def test_edit_librarian_info_view(self):
        # Test edit librarian info view
        self.client.login(username='admin', password='admin123')
        librarian = User.objects.create(username='librarian', email='librarian@example.com')
        response = self.client.post(reverse('editlibrarianinfo', args=[librarian.id]), {
            # Provide necessary form data here
        })
        self.assertEqual(response.status_code, 302)  # Example, modify as needed

    def test_delete_librarian_view(self):
        # Test delete librarian view
        self.client.login(username='admin', password='admin123')
        response = self.client.post(reverse('deletelibrarian', args=[1]))  # Provide a valid librarian ID
        self.assertEqual(response.status_code, 302)  # Example, modify as needed
