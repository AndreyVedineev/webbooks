from django.urls import path
from catalog import views

app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="authors_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my_borrowed"),
]
