from django import forms


class CategoryForm(forms.Form):
	name = forms.CharField(label='Category Name:', max_length=50,
							widget=forms.TextInput(attrs={'placeholder': ' '}))


class EditCategoryForm(forms.Form):
	pass


