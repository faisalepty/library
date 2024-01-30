from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('', views.Home, name='home'),
    path('Books/', views.BooksDetails, name='bookdetails'),
    path('members/', views.MembersDetails, name='membersdetails'),
    path('bookinfo/<str:pk>/', views.BookInfo, name='bookinfo'),
    path('memberinfo/<str:pk>/', views.MemberInfo, name='memberinfo'),
    path('newbook/', views.AddNewBook, name='addnewbook'),
    path('newmember/', views.AddNewMember, name='addnewmember'),
    path('issuebook/', views.IssueBook, name='issuebook'),
    path('editmemberinfo/<str:pk>', views.EditMemberInfo, name='editmemberinfo'),
    path('editbookinfo/<str:pk>', views.EditBookInfo, name='editbookinfo'),
    path('updatebookreturn/<str:pk>', views.bookReturn, name='updatebookreturn'),
    path('deletebook/<str:pk>', views.DeleteBook, name='deletebook'),
    path('deletemember/<str:pk>', views.DeleteMember, name='deletemember'),
               ]