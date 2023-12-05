from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункт меню'
