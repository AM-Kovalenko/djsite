from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото")
    time_created = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликованно")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)   # 'Category' в виде строки, тк класс определен ниже. Если до - то можно без кавычек

    #магический метод, который возвращает имя категории
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})

    class Meta:
        verbose_name='Известные женцины'
        verbose_name_plural='Известные женцины'
        ordering = ['time_created','title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    #магический метод, который возвращает имя категории
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering = ['id']
