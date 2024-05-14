from django.db import models


class Women(models.Model):  # Базовая модель
    title = models.CharField(max_length=255)  # заголовок
    content = models.TextField(blank=True)  # содержание
    time_create = models.DateTimeField(auto_now_add=True)  # дата создания
    time_update = models.DateTimeField(auto_now=True)  # дата обновления
    is_published = models.BooleanField(default=True)  # статус публикации
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # ссылка на таблицу "Категории"

    def __str__(self):
        return self.title


class Category(models.Model):  # Модель Категории с одним полем(name)
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


