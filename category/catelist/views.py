from django.shortcuts import render
from django.template import RequestContext

from .models import Category
from .forms import CategoryForm, EditCategoryForm


def categories(request):
    categories = Category.objects.all()
    form = CategoryForm()
    return render(request, 'categories.html', 
    			 {'nodes': categories, 'form': form})
  
def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = EditCategoryForm()
    return render(request, 'category.html', 
    	         {'category': category, 'form': form })