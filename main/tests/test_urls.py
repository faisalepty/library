from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main import views

class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, views.Login)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, views.Logout)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.Home)

    def test_books_details_url_resolves(self):
        url = reverse('bookdetails')
        self.assertEquals(resolve(url).func, views.BooksDetails)

    def test_members_details_url_resolves(self):
        url = reverse('membersdetails')
        self.assertEquals(resolve(url).func, views.MembersDetails)

    def test_book_info_url_resolves(self):
        url = reverse('bookinfo', args=['1'])
        self.assertEquals(resolve(url).func, views.BookInfo)

    def test_member_info_url_resolves(self):
        url = reverse('memberinfo', args=['1'])
        self.assertEquals(resolve(url).func, views.MemberInfo)

    def test_add_new_book_url_resolves(self):
        url = reverse('addnewbook')
        self.assertEquals(resolve(url).func, views.AddNewBook)

    def test_add_new_member_url_resolves(self):
        url = reverse('addnewmember')
        self.assertEquals(resolve(url).func, views.AddNewMember)

    def test_issue_book_url_resolves(self):
        url = reverse('issuebook')
        self.assertEquals(resolve(url).func, views.IssueBook)

    def test_edit_member_info_url_resolves(self):
        url = reverse('editmemberinfo', args=['1'])
        self.assertEquals(resolve(url).func, views.EditMemberInfo)

    def test_edit_book_info_url_resolves(self):
        url = reverse('editbookinfo', args=['1'])
        self.assertEquals(resolve(url).func, views.EditBookInfo)

    def test_update_book_return_url_resolves(self):
        url = reverse('updatebookreturn', args=['1'])
        self.assertEquals(resolve(url).func, views.bookReturn)

    def test_delete_book_url_resolves(self):
        url = reverse('deletebook', args=['1'])
        self.assertEquals(resolve(url).func, views.DeleteBook)

    def test_delete_member_url_resolves(self):
        url = reverse('deletemember', args=['1'])
        self.assertEquals(resolve(url).func, views.DeleteMember)

    def test_add_new_librarian_url_resolves(self):
        url = reverse('librarians')
        self.assertEquals(resolve(url).func, views.AddNewLibrarian)

    def test_edit_librarian_info_url_resolves(self):
        url = reverse('editlibrarianinfo', args=['1'])
        self.assertEquals(resolve(url).func, views.EditLibrarianInfo)

    def test_delete_librarian_url_resolves(self):
        url = reverse('deletelibrarian', args=['1'])
        self.assertEquals(resolve(url).func, views.DeleteLibrarian)
