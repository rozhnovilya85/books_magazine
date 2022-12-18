# Generated by Django 3.2 on 2022-12-03 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_firstname', models.CharField(max_length=100, verbose_name='Фамилия автора')),
                ('author_name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('author_patronymic', models.CharField(max_length=100, verbose_name='Отчетсво автора')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Биография')),
                ('photo', models.ImageField(null=True, upload_to='image/%Y/%m/%d', verbose_name='Фотография')),
                ('date_of_birth', models.DateField(verbose_name='День рождения')),
                ('date_of_death', models.DateField(blank=True, default=None, null=True, verbose_name='День смерти')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['author_firstname'],
            },
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Книга', max_length=120, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('pages', models.FloatField(default=10, verbose_name='Количество страниц')),
                ('price', models.FloatField(default=10, verbose_name='Цена')),
                ('cover_type', models.CharField(max_length=120, verbose_name='Тип обложки')),
                ('size', models.CharField(max_length=100, verbose_name='Размер')),
                ('date_publication', models.DateField(null=True, verbose_name='Дата публикации')),
                ('photo', models.ImageField(null=True, upload_to='image/%Y/%m/%d', verbose_name='Фотография')),
                ('date_update', models.DateField(auto_now=True, null=True, verbose_name='Дата изменения записи')),
                ('exist', models.BooleanField(default=True, verbose_name='В каталоге?')),
                ('status_book', models.CharField(choices=[('1', 'BESTSELLER'), ('2', 'HOT'), ('3', 'NEW'), ('4', 'SALE')], default='3', max_length=10, verbose_name='Статус')),
                ('authors', models.ManyToManyField(to='library.Author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=120, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('date_finish', models.DateTimeField(null=True, verbose_name='Дата завершения заказа')),
                ('price', models.FloatField(null=True, verbose_name='Стоимость заказа')),
                ('address_delivery', models.CharField(max_length=150, verbose_name='Адрес доставки')),
                ('status', models.CharField(choices=[('1', 'Создан'), ('2', 'Отменён'), ('3', 'Согласован'), ('4', 'В пути'), ('5', 'Завершен')], max_length=150, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['date_create'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название компании поставщика')),
                ('agent_firstname', models.CharField(max_length=100, verbose_name='Фамилия агента поставщика')),
                ('agent_name', models.CharField(max_length=100, verbose_name='Имя агента поставщика')),
                ('agent_patronymic', models.CharField(max_length=100, verbose_name='Отчетсво агента поставщика')),
                ('exist', models.BooleanField(default=True, verbose_name='Сотрудничаем?')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('date_print', models.DateTimeField(auto_now_add=True, verbose_name='Дата распечатки')),
                ('address_print', models.CharField(max_length=150, verbose_name='Место создание чека')),
                ('terminal', models.CharField(max_length=10, verbose_name='Код терминала')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='library.order')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чеки',
                'ordering': ['terminal', 'date_print'],
            },
        ),
        migrations.CreateModel(
            name='Pos_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_book', models.IntegerField(verbose_name='Количество книг')),
                ('price', models.IntegerField(verbose_name='Общая цена книг')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.book', verbose_name='Книга')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
                'ordering': ['book', 'order', 'price'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(through='library.Pos_order', to='library.book'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='library.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.supplier', verbose_name='Поставщик'),
        ),
    ]