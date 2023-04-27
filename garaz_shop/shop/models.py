from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#Экземпляры ContentType представляют и хранят информацию о моделях, установленных в проекте; новые экземпляры ContentType автоматически создаются каждый раз при установке новых шаблонов.
#GenericForeignKey - Добавьте ключ ForeignKey

# Категория, продукт, Карзина, Заказ, покупатель, Описание продукта


class Categoria(models.Model):

    name = models.CharField(max_length=255, verbose_name="Категория")
    ssylka = models.SlugField(unique=True) # ссылка категории

    def __str__(self):
        return self.name


class Product(models.Model):

    categoria = models.ForeignKey(Categoria, verbose_name="Категория", on_delete=models.CASCADE) # on_delete=models.CASCADE - для удаления объекта
    name_priduct = models.CharField(max_length=255, verbose_name="Наименование")
    artikul = models.CharField(max_length=255, verbose_name="Артикул")
    ssylka = models.SlugField(unique=True)  # ссылка на продукт
    image = models.ImageField()
    opisanie = models.TextField(null=True, verbose_name="Описание товара") # null=True описание может и не быть
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена") # max_digits=10 - максимальная длина числа до запятой, decimal_places=2 - количесво чисел после запятой

    class Meta:
        abstract = True  # Important

    def __str__(self):
        return self.name_priduct


class Oil_product(Product):

    valume = models.CharField(max_length=255, verbose_name="Объем")
    brand = models.CharField(max_length=255, verbose_name="Бренд")
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель")

    def __str__(self):
        return "{} {}".format(self.categoria.name, self.name_priduct)


class Filter_product(Product):

    size = models.CharField(max_length=255, verbose_name="Размер")
    brand = models.CharField(max_length=255, verbose_name="Бренд")
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель")

    def __str__(self):
        return "{} {}".format(self.categoria.name, self.name_priduct)


class Carsina_pocupok(models.Model):

    user = models.ForeignKey("Pocupatel", verbose_name="Пользователь", on_delete=models.CASCADE) # on_delete=models.CASCADE - для удаления объекта
    corzina = models.ForeignKey("Carsina", verbose_name="Корзина", on_delete=models.CASCADE) # on_delete=models.CASCADE - для удаления объекта
    product_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    id_product = models.PositiveIntegerField()
    content_product = GenericForeignKey("product_type", "id_product")
    colihestvo = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итог")

    def __str__(self):
        return self.product


class Carsina(models.Model):

    user_name = models.ForeignKey("Pocupatel", verbose_name="Пользователь", on_delete=models.CASCADE) # on_delete=models.CASCADE - для удаления объекта
    product = models.ManyToManyField(Carsina_pocupok, blank=True)
    colihextvo_productov = models.PositiveIntegerField(default=0)# для корректного вывода товаров в карзине
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итог")
    # ДОПИСАТЬ!!!
    #def __str__(self):
        #return self.

#ДОПИСАТЬ
#class Zakaz(models.Model):

#   УТОЧНИТЬ!!!!!
class Pocupatel(models.Model):

    #user = models.ForeignKey(verbose_name="Пользователь", on_delete=models.CASCADE)# необходимо передать данные из аккаунта регистрация
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    #email =
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return "Пользователь {} {}".format(self.lastname, self.firstname)


#class Spetification(models.Model):

    #id_tovara = models.PositiveIntegerField()
    #name = models.CharField(max_length=255, verbose_name="Наименование товара")

    #def __str__(self):
        #return self.name
