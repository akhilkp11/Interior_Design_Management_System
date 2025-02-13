from django.shortcuts import render, redirect
from AdminApp.models import CategoryDb, ProductDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.

def display_index(request):
    category = CategoryDb.objects.count
    product = ProductDb.objects.count
    return render(request, "index.html", {'category': category, 'product': product})


def add_category(request):
    return render(request, 'add_category.html')


def display_category(request):
    category = CategoryDb.objects.all()
    return render(request, "display_category.html", {'category': category})


def save_category(request):
    if request.method == "POST":
        na = request.POST.get('cat-name')
        # des = request.POST.get('description')
        img = request.FILES['cat-img']
        obj = CategoryDb(category_name=na, category_image=img)
        obj.save()
        return redirect(display_category)


def edit_category(request, ct_id):
    data = CategoryDb.objects.get(id=ct_id)
    return render(request, "edit_category.html", {'data': data})


def update_category(request, ct_id):
    if request.method == "POST":
        na = request.POST.get('cat-name')
        try:
            img = request.FILES['cat-img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=ct_id).category_image

        CategoryDb.objects.filter(id=ct_id).update(category_name=na, category_image=file)
    return redirect(display_category)


def delete_category(request, ct_id):
    data = CategoryDb.objects.get(id=ct_id)
    data.delete()
    return redirect(display_category)


def add_product(request):
    cat = CategoryDb.objects.all()
    return render(request, "add_product.html", {'cat': cat})


def display_product(request):
    data = ProductDb.objects.all()
    return render(request, "display_products.html", {'data': data})


def save_product(request):
    if request.method == "POST":
        pro_na = request.POST.get('pro_name')
        cat_na = request.POST.get('cat_name')
        sb_na = request.POST.get('sub_cat')
        des = request.POST.get('description')
        pr = request.POST.get('price')
        qty = request.POST.get('quantity')
        img = request.FILES['pro_img']
        obj = ProductDb(product_name=pro_na, category_name=cat_na, sub_category_name=sb_na,
                        Description=des, price=pr, quantity=qty, product_image=img)
        obj.save()
    return redirect(display_product)


def edit_product(request, pr_id):
    product = ProductDb.objects.get(id=pr_id)
    category = CategoryDb.objects.all()
    return render(request, "edit_product.html", {'data': product, 'category': category})


def update_product(request, pr_id):
    if request.method == "POST":
        pro_na = request.POST.get('pro_name')
        cat_na = request.POST.get('cat_name')
        sb_na = request.POST.get('sub_cat')
        des = request.POST.get('description')
        pr = request.POST.get('price')
        qty = request.POST.get('quantity')
        try:
            img = request.FILES['pro_img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=pr_id).product_image

        ProductDb.objects.filter(id=pr_id).update(product_name=pro_na, category_name=cat_na, sub_category_name=sb_na,
                                                  Description=des, price=pr, quantity=qty, product_image=file)
        return redirect(display_product)
