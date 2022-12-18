from django.db import models
from django.urls import reverse, reverse_lazy
# Create your models here.


# class Status_Book(models.Model):
#     status_book = models.CharField(max_length=10, verbose_name='Статус', choices=[('1', 'BESTSELLER'), ('2', 'HOT'), ('3', 'NEW'), ('4', 'SALE')], default='3')
#
#     def __str__(self):  # Переопределение названия объекта
#         return self.status_book
#
#     class Meta:  # Класс для названий нашей модели в админке
#         verbose_name = 'Статус'  # Надпись в единственном числе
#         verbose_name_plural = 'Статусы'  # Надпись во множественном числе
#         ordering = ['status_book']  # Сортировка полей (по возрастанию)


class Genre(models.Model):
    genre = models.CharField(max_length=120, verbose_name='Жанр')

    def __str__(self):  # Переопределение названия объекта
        return self.genre

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Жанр'  # Надпись в единственном числе
        verbose_name_plural = 'Жанры'  # Надпись во множественном числе
        ordering = ['genre']  # Сортировка полей (по возрастанию)


class Author(models.Model):
    author_firstname = models.CharField(max_length=100, verbose_name='Фамилия автора')
    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    author_patronymic = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчетсво автора')
    biography = models.TextField(blank=True, null=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Фотография')
    date_of_birth = models.DateField(verbose_name='День рождения')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='День смерти', default=None)

    def __str__(self):  # Переопределение названия объекта
        return f"{self.author_firstname}  {self.author_name}  {self.author_patronymic}"

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Автор'  # Надпись в единственном числе
        verbose_name_plural = 'Авторы'  # Надпись во множественном числе
        ordering = ['author_firstname']  # Сортировка полей (по возрастанию)

    # def __str__(self):
    #     if self.date_of_death == None:
    #         return f'{self.date_of_death = 'Жив по сей день'}'


class book(models.Model):
    name = models.CharField(max_length=120, default='Книга', verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    pages = models.FloatField(default=10, verbose_name='Количество страниц')
    price = models.FloatField(default=10, verbose_name='Цена')
    cover_type = models.CharField(max_length=120, verbose_name='Тип обложки')
    size = models.CharField(max_length=100, verbose_name='Размер')
    date_publication = models.DateField(null=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Фотография')
    date_update = models.DateField(auto_now=True, null=True, verbose_name='Дата изменения записи')
    exist = models.BooleanField(default=True, verbose_name='В каталоге?')

    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, null=True, verbose_name='Поставщик')
    authors = models.ManyToManyField(Author, verbose_name='Автор')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    # status_book = models.ForeignKey(Status_Book, on_delete=models.PROTECT, null=True, verbose_name='Статус книги')
    status_book = models.CharField(max_length=10, verbose_name='Статус',
                                   choices=[('BESTSELLER', 'BESTSELLER'), ('HOT', 'HOT'), ('NEW', 'NEW'), ('SALE', 'SALE')],
                                   default='NEW')

    def get_absolute_url(self):  # тэг url для объекта (Данный метод для вывода странички одной записи)
        return reverse('book_detail', kwargs={'book_id': self.pk})


    def __str__(self):  # Переопределение названия объекта
        return self.name

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Книга'  # Надпись в единственном числе
        verbose_name_plural = 'Книги'  # Надпись во множественном числе
        ordering = ['name']  # Сортировка полей (по возрастанию)


class Supplier(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название компании поставщика')
    agent_firstname = models.CharField(max_length=100, verbose_name='Фамилия агента поставщика')
    agent_name = models.CharField(max_length=100, verbose_name='Имя агента поставщика')
    agent_patronymic = models.CharField(max_length=100, verbose_name='Отчетсво агента поставщика')
    exist = models.BooleanField(default=True, verbose_name='Сотрудничаем?')

    def __str__(self):
        return self.title

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Поставщик'  # Надпись в единственном числе
        verbose_name_plural = 'Поставщики'  # Надпись во множественном числе
        ordering = ['title']  # Сортировка полей (по возрастанию)


class Order(models.Model):
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, verbose_name='Дата завершения заказа')
    price = models.FloatField(null=True, verbose_name='Стоимость заказа')
    address_delivery = models.CharField(max_length=150, verbose_name='Адрес доставки')
    status = models.CharField(max_length=150, verbose_name='Статус', choices=[('1', 'Создан'),
                                                                              ('2', 'Отменён'),
                                                                              ('3', 'Согласован'),
                                                                              ('4', 'В пути'),
                                                                              ('5', 'Завершен')])

    books = models.ManyToManyField(book, through='Pos_order')

    def __str__(self):
        return f"{self.date_create} | {self.status} | {self.price}"

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Заказ'  # Надпись в единственном числе
        verbose_name_plural = 'Заказы'  # Надпись во множественном числе
        ordering = ['date_create']  # Сортировка полей (по возрастанию)

class Pos_order(models.Model):
    book = models.ForeignKey(book, on_delete=models.PROTECT, verbose_name='Книга')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count_book = models.IntegerField(verbose_name='Количество книг')
    price = models.IntegerField(verbose_name='Общая цена книг')

    def __str__(self):
        return self.book.name + " " + self.order.address_delivery + " " + self.order.status


    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Позиция'  # Надпись в единственном числе
        verbose_name_plural = 'Позиции'  # Надпись во множественном числе
        ordering = ['book', 'order', 'price']  # Сортировка полей (по возрастанию)


class Cheque(models.Model):
    date_print = models.DateTimeField(auto_now_add=True, verbose_name='Дата распечатки')
    address_print = models.CharField(max_length=150, verbose_name='Место создание чека')
    terminal = models.CharField(max_length=10, verbose_name='Код терминала')

    order = models.OneToOneField(Order, on_delete=models.PROTECT, primary_key=True)


    def __str__(self):
        return str(self.date_print) + " " + self.terminal


    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Чек'  # Надпись в единственном числе
        verbose_name_plural = 'Чеки'  # Надпись во множественном числе
        ordering = ['terminal', 'date_print']  # Сортировка полей (по возрастанию)

















