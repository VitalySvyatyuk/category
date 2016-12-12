# -*- coding: utf-8 -*-
from django import forms
from .models import Category


class CategoryForm(forms.Form):
    """Формы на главной странице, позволяющая добавить новую категорию."""
    parent = forms.ChoiceField(label='Select Parent:', 
                            widget=forms.Select(attrs={'class': 'selectpicker'}), choices=())
    name = forms.CharField(label='New Category Name:', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': ' '}))

    def __init__(self, *args, **kwargs):
        """Данный метод инициализирует каталог категорий для поля parent, запрашивая данные из таблицы category_catelist."""
        super(CategoryForm, self).__init__(*args, **kwargs)
        PARENTS = [(0, " ")]
        for parent in Category.objects.all():
            PARENTS.append((parent.id, parent.name))
        self.fields['parent'].choices = PARENTS


class EditCategoryForm(forms.Form):
    """Форма для редактирования категории. Поле category_id скрыто. Оно необходимо для хранения идентификатора категории в БД."""
    name = forms.CharField(label='Category Name:', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': ' '}))
    category_id = forms.CharField(label='', max_length=3,
                            widget=forms.TextInput(attrs={'class': 'category_id'}))




