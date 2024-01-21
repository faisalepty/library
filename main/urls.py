from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Home, name='home'),
    path('Books/', views.BooksDetails, name='bookdetails'),
    path('bookInfo/<str:pk>', views.BookInfo, name='bookinfo'),
    path('newbook/', views.AddNewBook, name='addnewbook'),
    path('newmember/', views.AddNewMember, name='addnewmember'),
    path('editmemberinfo/<str:pk>', views.EditMemberInfo, name='editmemberinfo'),
    path('editbookinfo/<str:pk>', views.EditBookInfo, name='editbookinfo'),
    path('deletebook/<str:pk>', views.DeleteBook, name='deletebook'),
               ]