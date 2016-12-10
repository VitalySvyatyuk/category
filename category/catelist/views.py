from django.shortcuts import render
from django.template import RequestContext

from .models import Category
from .forms import CategoryForm, EditCategoryForm


def categories(request):
    if request.method == 'POST':
        already_exists = False
        name = request.POST['name']
        categories = Category.objects.all() 
        for catname in categories:
            if str(catname) == str(name):
                form = CategoryForm(request.POST)
                already_exists = True
                return render(request, 'categories.html', 
                             {'categories': categories, 
                              'form': form,
                              'already_exists': already_exists})  
        parent = request.POST['select-parent']
        if parent == "0":
            cat = Category(name=name)
            cat.save()
        else:
            parent = Category.objects.get(id=parent)
            cat = Category(name=name, parent=parent)
            cat.save()
        categories = Category.objects.all()
        form = CategoryForm()
        return render(request, 'categories.html', 
                     {'categories': categories, 'form': form})
    else:
        categories = Category.objects.all()
        form = CategoryForm()
        return render(request, 'categories.html', 
                     {'categories': categories, 'form': form})
  
def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = EditCategoryForm()
    return render(request, 'category.html', 
                 {'category': category, 'form': form })