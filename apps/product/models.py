from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('Название',max_length=50)
    price = models.DecimalField("Цена",max_digits=7, decimal_places=2)
    description = models.TextField("Описание")
    brand = models.CharField('Бренд',max_length=50)
    photo = models.ImageField("Фото", upload_to='images/')
    public_date = models.DateField("Дата публикации", auto_now_add=True)
    count = models.IntegerField("Количество", default=0)

# popytka



