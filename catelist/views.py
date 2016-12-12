# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import Category
from .forms import CategoryForm, EditCategoryForm


def categories(request):
    """Вьюха, обслуживающая главную стрицу. Принимает POST-запросы от обеих форм: с главной страницы и со страницы редактирования категории."""
    if request.method == 'POST':
        if '_delete' in request.POST:
            category = Category.objects.get(id=request.POST['category_id'])
            category.delete()
            return redirect("/")

        already_exists = False
        name = request.POST['name']
        categories = Category.objects.all() 
        for catname in categories:
            if str(catname) == str(name):
                if '_save' in request.POST:
                    form = CategoryForm()
                    return render(request, 'categories.html', 
                                 {'categories': categories, 'form': form})
                form = CategoryForm(request.POST)
                already_exists = True
                return render(request, 'categories.html', 
                             {'categories': categories, 
                              'form': form,
                              'already_exists': already_exists})  
        if 'parent' in request.POST:
            parent = request.POST['parent']
            print parent
            if parent == "0":
                cat = Category(name=name)
                cat.save()
            else:
                parent = Category.objects.get(id=parent)
                cat = Category(name=name, parent=parent)
                cat.save()
        elif '_save' in request.POST:
            cat = Category.objects.get(id=request.POST['category_id'])
            cat.name = request.POST['name']
            cat.save()
    else:
        pass
    categories = Category.objects.all()
    form = CategoryForm()
    return render(request, 'categories.html', 
                 {'categories': categories, 'form': form})
  
def category(request, category_id):
    """Вьюха для отображения страницы редактирования категории. Не обрабатывает POST-запросы."""
    category = Category.objects.get(pk=category_id)
    category_path = category.get_ancestors(ascending=False, include_self=True)
    form_data = {'name': category.name, 'category_id': category_id }
    form = EditCategoryForm(form_data)
    print category_path
    return render(request, 'category.html', 
                 {'category': category, 'form': form,
                  'category_path': category_path})
