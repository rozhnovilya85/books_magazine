from django.urls import path
from rest_framework import routers
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from library.views import index_all, index_books, book_detail, BookCreateView, supplier_form, SupplierCreateView, \
    BookListView, BookDetailView, user_registration, user_login, BookAdminListView, BookUpdateView, SupplireListView, \
    SupplireUpdateView, SupplierDeleteView, BookDeleteView, user_logout, send_contact_email, AuthorListView, \
    AuthorDetailView, AuthorAdminListView, book_api_list, BookViewSet, AuthorViewSet, AuthorCreateView, \
    AuthorUpdateView, AuthorDeleteView

router = routers.SimpleRouter()
router.register('book_class', BookViewSet)
router.register('author_class', AuthorViewSet)

urlpatterns = [
    path('index/books', index_books, name='books'),
    path('index/book/<int:book_id>', book_detail, name='book_detail'),
    path('index/books/booksform', BookCreateView.as_view(), name='book_form'),
    path('', BookListView.as_view(), name='index'),
    path('index/books/supp', supplier_form, name='supplier_form'),
    path('index/books/supplierform', SupplierCreateView.as_view(), name='supplier_form_class'),
    path('index/books/<int:book_id>', BookDetailView.as_view(), name='book_detail'),
    path('index/account/registration/', user_registration, name='registration'),
    path('index/account/auth/', user_login, name='auth'),
    path('index/account/books_admin/', BookAdminListView.as_view(), name='books_admin'),
    path('index/account/book_updete/<int:pk>', BookUpdateView.as_view(), name='books_update'),
    path('index/supplire/supplire_admin/', SupplireListView.as_view(), name='supplire_admin'),
    path('index/supplire/supplire_update/<int:pk>', SupplireUpdateView.as_view(), name='supplire_update'),
    path('index/supplire/supplire_delete/<int:pk>', SupplierDeleteView.as_view(), name='supplire_delete'),
    path('index/account/book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('index/account/logout/', user_logout, name='logout'),
    path('index/contact/', send_contact_email, name='contact'),
    path('index/authors/', AuthorListView.as_view(), name='authors'),
    path('index/authors/author_detail/<int:author_id>', AuthorDetailView.as_view(), name='author_detail'),
    path('index/authors/author_admin/', AuthorAdminListView.as_view(), name='author_admin'),
    path('index/authors/author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('index/supplire/author_update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('index/supplire/author_delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    path('api/books/', book_api_list, name='api_books'),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)