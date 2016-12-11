from django import forms

from .models import Category

PARENTS = []
for parent in Category.objects.all():
    PARENTS.append((parent.id, parent.name))
print PARENTS


class CategoryForm(forms.Form):
    parent = forms.ChoiceField(label='Select Parent:', 
                            widget=forms.Select, choices=PARENTS)
    name = forms.CharField(label='New Category Name:', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': ' '}))


class EditCategoryForm(forms.Form):
    name = forms.CharField(label='Category Name:', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': ' '}))
    category_id = forms.CharField(label='', max_length=3,
                                  widget=forms.TextInput(attrs={'class': 'category_id'}))


