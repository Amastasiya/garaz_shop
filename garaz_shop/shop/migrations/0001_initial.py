# Generated by Django 4.1.4 on 2023-04-27 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carsina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colihextvo_productov', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итог')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('ssylka', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pocupatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Oil_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_priduct', models.CharField(max_length=255, verbose_name='Наименование')),
                ('artikul', models.CharField(max_length=255, verbose_name='Артикул')),
                ('ssylka', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('opisanie', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('valume', models.CharField(max_length=255, verbose_name='Объем')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categoria', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Filter_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_priduct', models.CharField(max_length=255, verbose_name='Наименование')),
                ('artikul', models.CharField(max_length=255, verbose_name='Артикул')),
                ('ssylka', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('opisanie', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categoria', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Carsina_pocupok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.PositiveIntegerField()),
                ('colihestvo', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итог')),
                ('corzina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.carsina', verbose_name='Корзина')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.pocupatel', verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='carsina',
            name='product',
            field=models.ManyToManyField(blank=True, to='shop.carsina_pocupok'),
        ),
        migrations.AddField(
            model_name='carsina',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.pocupatel', verbose_name='Пользователь'),
        ),
    ]