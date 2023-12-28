from django.db import models

# Create your models here.

class Tovars(models.Model):
    Id_tovara = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    characteristic = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    maker = models.ForeignKey('Maker', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    categories = models.ManyToManyField('Categories')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





class Zakaz(models.Model):
    ID = models.ManyToManyField('Tovars')
    quantity = models.IntegerField()
    total_cost =  models.IntegerField()
    customer_name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.ID

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class Maker(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'




class Categories(models.Model):
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'