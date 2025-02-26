from django.shortcuts import render, redirect
from AdminApp.models import CategoryDb, ProductDb, DesignCategoryDb, DesignsDb
from WebApp.models import ContactDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.

def display_index(request):
    category = CategoryDb.objects.count
    product = ProductDb.objects.count
    booking = ContactDb.objects.count
    return render(request, "index.html", {'category': category, 'product': product, 'booking': booking})

# e-commerce side
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


def display_booking(request):
    data = ContactDb.objects.all()
    return render(request, "display_bookings.html", {'data': data})


# interior design side
def add_design_category(request):
    return render(request, "interior/add_design_category.html")


def save_design_category(request):
    if request.method == "POST":
        na = request.POST.get('cat-name')
        img = request.FILES['cat-img']
        obj = DesignCategoryDb(CategoryName=na, CategoryImage=img)
        obj.save()
        return redirect(display_design_category)


def display_design_category(request):
    data = DesignCategoryDb.objects.all()
    return render(request, "interior/display_design_category.html", {'data': data})


def add_designs(request):
    cat = DesignCategoryDb.objects.all()
    return render(request, "interior/add_designs.html", {'cat': cat})


def save_designs(request):
    if request.method == "POST":
        na = request.POST.get('design_name')
        designer = request.POST.get('designer')
        cat = request.POST.get('cat_name')
        description = request.POST.get('description')
        sty = request.POST.get('style')
        dim = request.POST.get('dimension')
        est = request.POST.get('estimate')
        img = request.FILES['design_img']
        obj = DesignsDb(Name=na, Designer=designer, Category=cat, Description=description, Style=sty,
                        Dimension=dim, Image=img, Estimate=est)
        obj.save()
        return redirect(display_designs)


def display_designs(request):
    data = DesignsDb.objects.all()
    return render(request, "interior/display_designs.html", {'data': data})


def edit_designs(request, d_id):
    data = DesignsDb.objects.get(id=d_id)
    cat = DesignCategoryDb.objects.all()
    return render(request, "interior/edit_designs.html", {'data': data, 'cat': cat})


def update_designs(request, d_id):
    if request.method == "POST":
        na = request.POST.get('design_name')
        designer = request.POST.get('designer')
        cat = request.POST.get('cat_name')
        description = request.POST.get('description')
        sty = request.POST.get('style')
        dim = request.POST.get('dimension')
        est = request.POST.get('estimate')
        try:
            img = request.FILES['design_img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = DesignsDb.objects.get(id=d_id).Image

        DesignsDb.objects.filter(id=d_id).update(Name=na, Designer=designer, Category=cat, Description=description,
                                                 Style=sty, Dimension=dim, Estimate=est, Image=file)
    return redirect(display_designs)


def delete_designs(request, d_id):
    x = DesignsDb.objects.get(id=d_id)
    x.delete()
    return redirect(display_designs)
