from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# данная функция нужна для ссылки /.../.../
def get_product_urls(object, vuewname):
   ct_model = object.__class__.meta.model.name
   return reverse(vuewname, kwargs={'ct_model': ct_model,
                                    'ssylka': object.slug})

# Покупатель
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE),
    is_active = models.BooleanField(default=True, verbose_name='Активность пользователя'),
    customer_orders = models.ManyToManyField('Order', blank=True, verbose_name='Заказы покупателя', related_name='related_customer')
    wishlist = models.ManyToManyField('Product', blank=True, verbose_name='Список ожидаемого')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')

    def __str__(self):
        return "Пользователь {}".format(self.user.first_name)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


# Категория
class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(unique=True)  # ссылка категории

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)# on_delete=models.CASCADE - для удаления объекта
    name_product = models.CharField(max_length=255, verbose_name="Наименование")
    artikul = models.CharField(max_length=255, verbose_name="Артикул")
    slug = models.SlugField(unique=True)  # ссылка на продукт
    image = models.ImageField(upload_to='media', verbose_name="Фотография")
    description = models.TextField(null=True, verbose_name="Описание товара")# null=True описание может и не быть
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")# max_digits=10 - максимальная длина числа до запятой, decimal_places=2 - количесво чисел после запятой

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Oil(Product):

    valume = models.CharField(max_length=255, verbose_name='Объем')

    def __str__(self):
        return "{} {}".format(self.category.name, self.name_product)

    def get_absolut_url(self):
        return get_product_urls(self, 'product_detail')

    class Meta:
        verbose_name = 'Масло'
        verbose_name_plural = 'Масла'


class Filter(Product):
    size = models.CharField(max_length=255, verbose_name='Размер')

    def __str__(self):
        return "{} {}".format(self.category.name, self.name_product)

    def get_absolut_url(self):
        return get_product_urls(self, 'product_detail')

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтра'


# Промежуточный продукт для корзины
class ProductCart(models.Model):
    guest = models.ForeignKey(Customer, verbose_name='Пользователь', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    # Content Types сохраняет информацию о моделях в таблицу contenttypes, а именно: название приложения, название модели и тип.
    # Таким образом мы можем создать GenericForeignKey на любую модель используя всего одно поле.
    # content_type, content_id, content_object - для расширения не только товаров, но и услуг
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')
    quantity = models.PositiveIntegerField(default=1)# Количество
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")# max_digits=10 - максимальная длина числа до запятой, decimal_places=2 - количесво чисел после запятой

    def __str__(self):
        return self.content_object.name

    # Функция для посчета итоговой цены
    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.content_object.price
        # return self.final_price - зациклился
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт для корзины'
        verbose_name_plural = 'Продукты для корзины'

# Корзина
class Cart(models.Model):
    guest = models.ForeignKey(Customer, verbose_name='Пользователь', on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCart, blank=True, related_name='related_cart', verbose_name='Продукты')# blank=True определяет, будет ли поле обязательным в формах. Сюда входят администраторские и ваши собственные пользовательские формы.
    product_quantity = models.IntegerField(default=8, verbose_name='Итоговое количество товара')
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")  # max_digits=10 - максимальная длина числа до запятой, decimal_places=2 - количесво чисел после запятой
    # является ли данная карзина какого либо товара
    order_in = models.BooleanField(default=False)
    # данное значения для пользователя который был не зарегистрирован
    user_anonym = models.BooleanField(default=False)

    def __str__(self):
        return self.products

    # Функция для подсчета суммы
    def product_sum(self):
        return [product.content_object for product in self.products.all()]

    # total_price = sum(book.price for book in Book.objects.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

# Заказы
class Order(models.Model):

    # статус заказа
    STATUS_NEW = 'new'
    # добавить заказ отменен
    STATUS_CANCELLED = 'cancelled'
    # в процессе
    STATUS_IN_PROGRESS = 'in_progress'
    # готов к выдаче
    STATUS_READY = 'is_ready'
    # выдан
    STATUS_COMPLETED = 'completed'

    # способ доставки
    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_CANCELLED, 'Заказ отменен'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ получен покупателем')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField(max_length=100, verbose_name='Тип заказа', choices=BUYING_TYPE_CHOICES)
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateField(verbose_name='Дата создания заказа', auto_now=True)
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


