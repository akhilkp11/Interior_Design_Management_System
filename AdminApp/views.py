from django.shortcuts import render, redirect, get_object_or_404
from AdminApp.models import CategoryDb, ProductDb, DesignCategoryDb, DesignsDb, DailyProgressDb
from WebApp.models import ContactDb, UserRegistrationDb
from DesignApp.models import ConsultDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def admin_login_page(request):
    return render(request, "admin_login_page.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username__contains=username).exists():
            x = authenticate(username=username, password=password)
            if x is not None:
                login(request, x)
                # session creation
                request.session['username'] = username
                request.session['password'] = password
                messages.success(request, "Welcome to  Admin Dashboard..!!")
                return redirect(display_index)
            else:
                messages.error(request, "Incorrect password..!!")
                return redirect(admin_login_page)
        else:
            messages.error(request, "Incorrect username..!!")
            return redirect(admin_login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)


def display_index(request):
    category = CategoryDb.objects.count
    product = ProductDb.objects.count
    booking = ContactDb.objects.count
    designs = DesignsDb.objects.count
    design_consultation = ConsultDb.objects.count

    context = {'category': category, 'product': product, 'booking': booking, 'designs': designs, 'design_consultation': design_consultation}
    return render(request, "index.html", context)

# e-commerce side
def add_category(request):
    return render(request, 'add_category.html')


def display_category(request):
    category = CategoryDb.objects.all()
    return render(request, "display_category.html", {'category': category})


def save_category(request):
    if request.method == "POST":
        na = request.POST.get('cat-name')

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


def delete_product(request, pr_id):
    x =ProductDb.objects.get(id=pr_id)
    x.delete()
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


def edit_design_category(request, d_id):
    data = DesignCategoryDb.objects.get(id=d_id)
    return render(request, "interior/edit_design_category.html", {'data': data})


def update_design_category(request, d_id):
    if request.method == "POST":
        na = request.POST.get('cat-name')
        try:
            img = request.FILES['cat-img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = DesignCategoryDb.objects.get(id=d_id).CategoryImage

        DesignCategoryDb.objects.filter(id=d_id).update(CategoryName=na, CategoryImage=file)
    return redirect(display_design_category)


def delete_design_category(reqest, d_id):
    x = DesignCategoryDb.objects.get(id=d_id)
    x.delete()
    return redirect(display_design_category)


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


def display_consultation(request):
    data = ConsultDb.objects.all()
    return render(request, "interior/display_consultation.html", {'data': data})


def book_consult_status(request, c_id):     # update ConsultDb status to booked
    obj = ConsultDb.objects.get(id=c_id)
    obj.status = 'booked'
    obj.save()
    return redirect(display_consultation)


def work_progress(reqest, c_id):
    # Safely fetch the ConsultDb instance or return 404 if it doesn't exist
    consult = get_object_or_404(ConsultDb, id=c_id)
    # Fetch all DailyProgressDb entries related to the consult and order by TimeStamp in reverse
    data = DailyProgressDb.objects.filter(consult=consult).order_by('-TimeStamp')
    return render(reqest, "interior/work_update.html", {'consult': consult, 'data': data})


def save_daily_progress(request, c_id):
    if request.method == 'POST':
        work_details = request.POST.get('work_details')  # Get work details from the form
        work_image = request.FILES.get('work_image')  # Get uploaded image

        # Assuming you have a consult instance (you may get it dynamically depending on your use case)
        consult = ConsultDb.objects.get(id=c_id)  # Or use appropriate logic to fetch the consult

        # Create and save the DailyProgressDb instance
        obj = DailyProgressDb(WorkDetails=work_details, WorkImage=work_image, consult=consult)
        obj.save()
        return redirect(display_consultation)


def complete_consult_status(request, c_id):
    obj = ConsultDb.objects.get(id=c_id)
    obj.status = 'completed'
    obj.save()
    return redirect(display_consultation)


def display_users(request):
    data = UserRegistrationDb.objects.all()
    return render(request, "display_users.html", {'data': data})


def edit_users(request, u_id):
    data = UserRegistrationDb.objects.get(id=u_id)
    return render(request, "edit_users.html", {'data': data})

def update_user(request, u_id):
    un = request.POST.get('username')
    ps1 = request.POST.get('password')
    ps2 = request.POST.get('conf_password')
    em = request.POST.get('email')
    cont = request.POST.get('contact')
    if ps1 != ps2:
        messages.error(request, "Passwords do not match.")
        return redirect(display_users)
    UserRegistrationDb.objects.filter(id=u_id).update(username=un, password=ps1, conf_password=ps2, email=em, contact=cont)
    return redirect(display_users)


def delete_user(request, u_id):
    x = UserRegistrationDb.objects.get(id=u_id)
    x.delete()
    return redirect(display_users)
