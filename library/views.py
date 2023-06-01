
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.db.models import Max, Min
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.base import View

from blog.models import Post
from .forms import BookForm, SupplierForm, ContactForm, AuthorForm

from django.shortcuts import render, redirect

from django.db.models import Q

# Create your views here.
from library.models import book, Supplier, Author, Genre
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from basket.forms import BasketAddProductForm
from .serializers import BookSerializer, AuthorSerializer


class GenreAuthor:

    def get_genres(self):
        return Genre.objects.all()

    def get_authors(self):
        return Author.objects.all()

    def get_status_books(self):
        queryset = book.objects.all()
        status_list = []
        for item in queryset:
            status_list.append(item.status_book)
        unique_status = set(status_list)
        return unique_status

    def get_price_books(self):
        price = book.objects.aggregate(Max('price'), Min('price'))
        return price


class FilterBooksView(GenreAuthor, ListView):
    model = book
    template_name = 'library/book_filter.html'
    def get_queryset(self):
        queryset = book.objects.filter(
            Q(authors__in=self.request.GET.getlist('authors'))|
            Q(genres__in=self.request.GET.getlist('genre'))|
            Q(status_book__in=self.request.GET.getlist('status'))).distinct()
        return queryset


class AuthorListView(ListView):
    model = Author
    template_name = 'library/author.html'
    context_object_name = 'authors_list'
    extra_context = {'title': 'Авторы книг'}
    paginate_by = 8


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author_item'
    extra_context = {'title': 'Автор книг'}
    pk_url_kwarg = 'author_id'
    allow_empty = False


class AuthorAdminListView(ListView):
    model = Author
    template_name = 'library/authors_admin.html'
    context_object_name = 'authors_list'
    extra_context = {'title': 'Администрирование авторов'}
    paginate_by = 8


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    context_object_name = 'form'
    extra_context = {'title': 'Создание записи автор'}
    success_url = reverse_lazy('author_admin')

    @method_decorator(permission_required('library.add_author'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_update.html'
    context_object_name = 'form'
    extra_context = {'title': 'Редактирование записи автор'}
    success_url = reverse_lazy('author_admin')

    @method_decorator(permission_required('library.change_author'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_admin')

    @method_decorator(permission_required('library.delete_author'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BookListView(ListView):
    model = book
    template_name = 'library/index.html'
    context_object_name = 'books_list'
    books_list_new = book.objects.all()
    # post_list = Post.objects.all()
    extra_context = {'title': 'Главная страница', 'books': books_list_new}
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = super(BookListView, self).get_context_data(**kwargs)
        object_list['post_list'] = Post.objects.all()[0:3]
        return object_list


class BookListFilterView(GenreAuthor, ListView):
    model = book
    template_name = 'library/book_list.html'
    context_object_name = 'books_list'
    extra_context = {'title': 'Поиск'}


class BookDetailView(GenreAuthor, DetailView):
    model = book
    template_name = 'library/book_detail.html'
    context_object_name = 'book_item'
    form = BasketAddProductForm()
    pk_url_kwarg = 'book_id'
    books = book.objects.all()
    extra_context = {'form_basket': form, 'title': 'Подробнее', 'books': books}
    allow_empty = False




class BookCreateView(CreateView):
    model = book
    form_class = BookForm  # Определение формы для взаимодействия
    template_name = 'library/book_form.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    extra_context = {'title': 'Создание записи книга'}
    success_url = reverse_lazy('books_admin')

    @method_decorator(permission_required('library.add_book'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'library/supplier_form.html'
    context_object_name = 'form'
    extra_context = {'title': 'Создание записи поставщик'}
    success_url = reverse_lazy('supplire_admin')

    @method_decorator(permission_required('library.add_supplier'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BookUpdateView(UpdateView):
    model = book
    form_class = BookForm
    template_name = 'library/book_updete.html'
    context_object_name = 'form'
    extra_context = {'title': 'Редактирование книг'}
    success_url = reverse_lazy('books_admin')

    @method_decorator(permission_required('library.change_book'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BookAdminListView(ListView):
    model = book
    template_name = 'library/book_admin.html'
    context_object_name = 'books_list'
    extra_context = {'title': 'Администрирование книг'}
    paginate_by = 4

    @method_decorator(permission_required('library.view_book'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SupplireListView(ListView):
    model = Supplier
    template_name = 'library/supplier_admin.html'
    context_object_name = 'supplier_list'
    extra_context = {'title': 'Администрирование поставщиков'}

    @method_decorator(permission_required('library.view_supplier'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SupplireUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'library/supplire_updete.html'
    context_object_name = 'form'
    extra_context = {'title': 'Редактирование поставщиков'}
    success_url = reverse_lazy('supplire_admin')

    @method_decorator(permission_required('library.change_supplier'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplire_admin')

    @method_decorator(permission_required('library.delete_supplier'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BookDeleteView(DeleteView):
    model = book
    success_url = reverse_lazy('books_admin')

    @method_decorator(permission_required('library.delete_book'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




def user_registration(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('registration')
        else:
            messages.error(request, 'Не удалось зарегистрировать!')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()
        context = {'form': form}
    return render(request, template_name='library/account.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'library/auth.html', {'form_l': form})


def user_logout(request):
    logout(request)
    return redirect('index')




def index_template(request):
    return render(request, 'base.html')


def index_all(request):
    books = book.objects.all()
    context = {
        'books_list': books,
    }
    return render(request=request, template_name='library/index.html', context=context)


def index_books(request):
    books = book.objects.all()
    context = {
        'books_list': books,
    }
    return render(request=request, template_name='library/books.html', context=context)


def book_detail(request, book_id):
    books = book.objects.get(pk=book_id)
    context = {'book_item': books}
    return render(request=request, template_name='library/book_detail.html', context=context)


def supplier_form(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            Supplier.objects.create(
                title=form.cleaned_data['title'],
                agent_name=form.cleaned_data['agent_name'],
                agent_firstname=form.cleaned_data['agent_firstname'],
                agent_patronymic=form.cleaned_data['agent_patronymic'],
                exist=form.cleaned_data['exist'],
            )
            # ==
            # Supplier.objects.create(
            #     **form.cleaned_data
            # )

            # return HttpResponseRedirect('/fruit/supplier/add/') # в методе указ. URL-адрес
            return redirect('index')  # в методе указ. URL-адрес, название пути, модель
        else:
            context = {'form': form}
            return render(request, 'library/supplier_form.html', context)
    else:
        form = SupplierForm()
        context = {'form': form}
        return render(request, 'library/supplier_form.html', context)

@login_required
def is_login_decorator(request):
    return HttpResponse('<h1>Зарегестрированны</h1>')


def error_404(request, exception):

    context = {'title': 'Вы попали на несуществующую страницу'}
    response = render(request, 'library/error404.html', context)
    response.status_code = 404
    return response


def send_contact_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(  # Отправка письма
                form.cleaned_data['subject'],  # Заголовок письма
                form.cleaned_data['content'],  # Тело письма
                settings.EMAIL_HOST_USER,  # Отправитель письмо
                ['rozhnov85@mail.ru'],
                # (form.cleaned_data['recipient'],),  # Получатель письма
                fail_silently=False,  # Режим отображения ошибок (True - исключения не будет)
                #                               (False - исключения выведутся на страницу)
            )
            if mail:
                messages.success(request, 'Письмо было успешно отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Письмо не удалось успешно отправить')
        else:
            messages.error(request, 'Письмо заполнено неверно')
    else:
        form = ContactForm()
    return render(request, 'library/contact.html', {'title': 'Предложения и пожелания', 'form': form})





# API

class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.filter(exist=True)
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view(['GET', 'POST'])
def book_api_list(request):
    if request.method == 'GET':
        books = book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse({'books_list': serializer.data})
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



