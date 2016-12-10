from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(label='Category Name:', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': ' '}))


class EditCategoryForm(forms.Form):
    name = forms.CharField(label='Category Name:', max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': ' '}))
    category_id = forms.CharField(label='', max_length=3,
                                  widget=forms.TextInput(attrs={'class': 'category_id'}))


