from django.db import models


class Category(models.Model):
    Name = models.CharField(max_length=255, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return 'Категория %s' % self.Name


class Subcategory(models.Model):
    Name = models.CharField(max_length=64, verbose_name='Наименование группы товаров')
    Prise = models.IntegerField(default=0, verbose_name='Стоимость группы товаров')
    Quantity = models.IntegerField(default=0, verbose_name='Колличество товаров в группе')
    Show = models.BooleanField(default=False, verbose_name='Видимость для менеджера')
    Activity = models.BooleanField(default=False, verbose_name='Активность на витрине')

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'

    def __str__(self):
        return 'Группа товаров %s' % self.Name


class Good(models.Model):
    Name = models.CharField(max_length=64, verbose_name='Наименование товаров')
    Description = models.TextField(verbose_name='Описание')
    Photo = models.CharField(blank=True, max_length=255, verbose_name='Ссылка на фото')
    Price = models.FloatField(verbose_name='Цена')
    Data = models.DateField(auto_now=True, verbose_name='Дата добавления')

    Category = models.ForeignKey(Category, blank=True)
    Subcategory = models.ForeignKey(Subcategory, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return 'Товар %s' % self.Name