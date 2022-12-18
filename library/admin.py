from django.contrib import admin
from .models import book, Supplier, Order, Pos_order, Cheque, Author, Genre


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'pages', 'price', 'cover_type', 'size', 'date_publication', 'supplier', 'photo', 'exist')
    list_display_links = ('id', 'name')
    list_editable = ('supplier',)
    filter_horizontal = ['authors', 'genres']


admin.site.register(book, BookAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'agent_firstname', 'agent_name', 'agent_patronymic', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'agent_firstname')
    list_editable = ('exist',)
    list_filter = ('exist',)


admin.site.register(Supplier, SupplierAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_create', 'date_finish', 'price', 'address_delivery', 'status')
    list_display_links = ('id', 'date_create')

admin.site.register(Order, OrderAdmin)

class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'order', 'count_book', 'price')
    list_display_links = ('book', 'order')
    search_fields = ('book', 'order')


admin.site.register(Pos_order, Pos_orderAdmin)



class ChequeAdmin(admin.ModelAdmin):
    list_display = ('order', 'date_print', 'address_print', 'terminal')
    list_display_links = ('order', 'date_print')
    search_fields = ('date_print', 'address_print')


admin.site.register(Cheque, ChequeAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_firstname', 'author_name', 'author_patronymic', 'biography', 'photo', 'date_of_birth', 'date_of_death')  # Отображение полей
    list_display_links = ('author_firstname',)  # Установка ссылок на атрибуты
    search_fields = ('author_firstname',)  # Поиск по полям
    # list_editable = ()  # Изменяемое поле
    list_filter = ('author_firstname',)  # Фильтры полей


admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    list_display_links = ('genre',)
    search_fields = ('genre',)  # Поиск по полям
    list_filter = ('genre',)  # Фильтры полей


admin.site.register(Genre, GenreAdmin)


# class Status_BookAdmin(admin.ModelAdmin):
#     list_display = ('status_book',)
#     list_display_links = ('status_book',)
#     search_fields = ('status_book',)  # Поиск по полям
#     list_filter = ('status_book',)  # Фильтры полей
#
# admin.site.register(Status_Book, Status_BookAdmin)

