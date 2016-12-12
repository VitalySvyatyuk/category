# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Основная и единственная модель, наследуется от mptt, что позволяет хранить данные в БД по алгоритму Modified Preorder Tree Traversal."""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        """Дополнительные настройки класса. Указан порядок - алфавитный."""
        order_insertion_by = ['name']

    def __str__(self):
        """Метод, позволяющий выводить ответ из БД с именем поля для наглядности."""
        return self.name



