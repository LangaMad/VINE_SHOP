from django.db import models
from .. accounts.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField('Название',max_length=50)
    price = models.DecimalField("Цена",max_digits=5, decimal_places=2)
    description = models.TextField("Описание")
    brand = models.CharField('Бренд',max_length=50)
    photo = models.ImageField("Фото", upload_to='images/')
    public_date = models.DateField("Дата публикации", auto_now_add=True)
    count = models.IntegerField("Количество", default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField('Category',max_length=100)
    photo = models.ImageField('Photo', upload_to='category/' , blank=True , null=True)
    product = models.ForeignKey(Product, blank=True , null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title





