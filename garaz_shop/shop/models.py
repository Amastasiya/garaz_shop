from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#Экземпляры ContentType представляют и хранят информацию о моделях, установленных в проекте; новые экземпляры ContentType автоматически создаются каждый раз при установке новых шаблонов.
#GenericForeignKey - Добавьте ключ ForeignKey
from django.urls import reverse

# Категория, продукт, Карзина, Заказ, покупатель, Описание продукта

def get_product_urls(object, vuewname):
   ct_model = object.__class__.meta.model.name
   return reverse(vuewname, kwargs={'ct_model': ct_model,
                                    'ssylka': object.ssylka})


class Pocupatel(models.Model):

    #user = models.ForeignKey(verbose_name="Пользователь", on_delete=models.CASCADE)# необходимо передать данные из аккаунта регистрация
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    #phone_number = PhoneNumberField(uniaue=True, verbose_name="Номер телефона")
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return "Пользователь {} {}".format(self.lastname, self.firstname)


class Categoria(models.Model):

    name = models.CharField(max_length=255, verbose_name="Категория")
    ssylka = models.SlugField(unique=True)  # ссылка категории

    def __str__(self):
        return self.name


class Product(models.Model):

    categoria = models.ForeignKey(
        Categoria,
        verbose_name="Категория",
        on_delete=models.CASCADE) # on_delete=models.CASCADE - для удаления объекта
    name_product = models.CharField(max_length=255, verbose_name="Наименование")
    artikul = models.CharField(max_length=255, verbose_name="Артикул")
    ssylka = models.SlugField(unique=True)  # ссылка на продукт
    image = models.ImageField(upload_to='media', verbose_name="Фотография")
    opisanie = models.TextField(null=True, verbose_name="Описание товара") # null=True описание может и не быть
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена") # max_digits=10 - максимальная длина числа до запятой, decimal_places=2 - количесво чисел после запятой

    #class Meta:
    #    abstract = True  # Important

    def __str__(self):
        return self.name_product


class Oil_product(Product):

    valume = models.CharField(max_length=255, verbose_name="Объем")
    brand = models.CharField(max_length=255, verbose_name="Бренд")
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель")

    def __str__(self):
        return "{} {}".format(self.categoria.name, self.name_product)

    def get_absolut_url(self):
        return get_product_urls(self, 'product_detail')


class Filter_product(Product):

    size = models.CharField(max_length=255, verbose_name="Размер")
    brand = models.CharField(max_length=255, verbose_name="Бренд")
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель")

    def __str__(self):
        return "{} {}".format(self.categoria.name, self.name_product)

#    def get_absolut_url(self):
#        return get_product_urls(self, 'product_detail')



class Carsina(models.Model):
#
    user = models.ForeignKey(
        to=Pocupatel,
        verbose_name="Пользователь",
        on_delete=models.CASCADE) # on_delete=models.CASCADE - для удаления объекта
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE)
    colihestvo = models.PositiveIntegerField(default=1)

    #def __str__(self):
    #    return self.product

    # ДОПИСАТЬ!!!
    #def __str__(self):
        #return self.

#ДОПИСАТЬ
#class Zakaz(models.Model):

#   УТОЧНИТЬ!!!!!

#class Spetification(models.Model):

    #id_tovara = models.PositiveIntegerField()
    #name = models.CharField(max_length=255, verbose_name="Наименование товара")

    #def __str__(self):
        #return self.name
