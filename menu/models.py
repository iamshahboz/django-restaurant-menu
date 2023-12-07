from django.db import models


class Menu(models.Model):
    name = models.CharField('Название меню', max_length=100, unique=True)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Название меню'
        verbose_name_plural = 'Название меню'


class MenuItem(models.Model):
    name = models.CharField('Пункт меню', max_length=50, unique=True)
    description = models.TextField('Описание', blank=True, null=True)
    url = models.URLField('Ссылка', max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункт меню'
