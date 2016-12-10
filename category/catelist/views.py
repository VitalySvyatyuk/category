from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import Category
from .forms import CategoryForm, EditCategoryForm


def categories(request):
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
                form = CategoryForm(request.POST)
                already_exists = True
                return render(request, 'categories.html', 
                             {'categories': categories, 
                              'form': form,
                              'already_exists': already_exists})  
        if 'select-parent' in request.POST:
            parent = request.POST['select-parent']
            if parent == "0":
                cat = Category(name=name)
                cat.save()
            else:
                parent = Category.objects.get(id=parent)
                cat = Category(name=name, parent=parent)
                cat.save()
            print "Select-parent"
        elif '_save' in request.POST:
            # cat = Category.objects.get(name=request.POST['name'])
            print "Save"


        categories = Category.objects.all()
        form = CategoryForm()
        return render(request, 'categories.html', 
                     {'categories': categories, 'form': form})


        return render(request, 'categories.html', 
                     {'categories': categories, 'form': form})
    else:
        categories = Category.objects.all()
        form = CategoryForm()
        return render(request, 'categories.html', 
                     {'categories': categories, 'form': form})
  
def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    # if request.method == 'POST':
    #     if '_save' in request.POST:
    #         if category.name != request.POST['name']:
    #             category.name = request.POST['name']
    #             category.save()
    #     elif '_delete' in request.POST:
    #         category.delete()
    #     return redirect(categories)

    form_data = {'name': category.name, 'category_id': category_id }
    form = EditCategoryForm(form_data)
    return render(request, 'category.html', 
                 {'category': category,
                  'form': form})
