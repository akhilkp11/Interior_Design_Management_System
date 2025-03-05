from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from AdminApp.models import CategoryDb, ProductDb
from WebApp.models import UserRegistrationDb, CartDb, OrderDb, ContactDb
from django.contrib import messages
import razorpay

# Create your views here.

def signup_page(request):
    return render(request, "signup.html")


def user_signup(request):
    if request.method == "POST":
        un = request.POST.get('user')
        ps1 = request.POST.get('password')
        ps2 = request.POST.get('re_password')
        em = request.POST.get('email')
        cont = request.POST.get('mobile')

        if ps1 != ps2:
            messages.error(request, "Passwords do not match.")
            return redirect(signup_page)

        if UserRegistrationDb.objects.filter(username=un).exists():
            messages.error(request, "Username already taken. Please choose another one.")

        obj = UserRegistrationDb(username=un, password=ps1, conf_password=ps2, email=em, contact=cont)
        obj.save()
        return redirect(signup_page)


# Create your login view function
def user_login(request):
    if request.method == "POST":
        # Get the data from the form
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        # Authenticate user
        if UserRegistrationDb.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            request.session['password'] = password
            messages.success(request, "Welcome to Heavenly Home")
            return redirect(display_home)
        else:
            messages.warning(request, "Invalid username or password")

            return redirect(signup_page)
    else:
        messages.warning(request, "Invalid username")
        return redirect(signup_page)


def user_sign_out(request):
    del request.session['username']
    del request.session['password']
    return redirect(display_home)


def display_home(request):
    return render(request, "home.html")

def save_contact_homepage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get('email')
        msg = request.POST.get('message')
        obj = ContactDb(Name=name, Email=mail, Message=msg)
        obj.save()
        return redirect(display_home)



# E-Commerce section
def display_shop(request):
    data = CategoryDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    return render(request, "shop_page.html", {'data': data, 'cart_count': cart_count})


def all_products(request):
    products = ProductDb.objects.all()
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    return render(request, "all_products.html", {'products': products, 'cart_count': cart_count})


def filtered_products(request, cat):
    data = ProductDb.objects.filter(category_name=cat)
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    category = cat
    return render(request, "filtered_products.html", {'data': data, 'category': category, 'cart_count': cart_count})


def single_product(request, pr_id):
    item = ProductDb.objects.get(id=pr_id)
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    return render(request, "single_product.html", {'item': item, 'cart_count': cart_count})


def save_cart(request):
    if request.method == "POST":
        un = request.POST.get('userName')
        pn = request.POST.get('productName')
        qty = request.POST.get('quantity')
        pri = request.POST.get('price')
        tot = request.POST.get('total')
        try:
            obj = ProductDb.objects.get(product_name=pn)
            img = obj.product_image
        except ProductDb.DoesNotExist:
            img = None
        cart = CartDb(Username=un, ProductName=pn, Quantity=qty, Price=pri, TotalPrice=tot, Pro_Image=img)
        cart.save()
        return redirect(display_shop)


def delete_cart_item(request, c_id):
    x = CartDb.objects.get(id=c_id)
    x.delete()
    return redirect(cart_page)


def cart_page(request):

    sub_total = 0
    Discount = 0
    total = 0
    data = CartDb.objects.filter(Username=request.session['username'])
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    for i in data:
        sub_total += i.TotalPrice

    if sub_total > 100000:
        Discount = sub_total*(5/100)
    else:
        Discount = sub_total*(1/100)

    total = sub_total - Discount

    context = {
        'data': data,
        'sub_total': sub_total,
        'Discount': Discount,
        'total': total,
        'cart_count': cart_count
    }
    return render(request, "cart.html", context)


def return_policy(request):
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    return render(request, "return_policy.html", {'cart_count': cart_count})


def checkout(request):
    sub_total = 0
    Discount = 0
    total = 0

    data = CartDb.objects.filter(Username=request.session['username'])
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    for i in data:
        sub_total += i.TotalPrice

    if sub_total > 100000:
        Discount = sub_total * (5 / 100)
        shipping_amount = 500
    else:
        Discount = sub_total * (1 / 100)
        shipping_amount = 1000

    total = int(sub_total - Discount + shipping_amount)


    context = {
        'data': data,
        'sub_total': sub_total,
        'Discount': Discount,
        'shipping_amount': shipping_amount,
        'total': total,
        'cart_count': cart_count
    }
    return render(request, "checkout.html", context)


def save_order(request):
    if request.method == "POST":
        name = request.POST.get('c_name')
        address = request.POST.get('c_address')
        ship_address = request.POST.get('c_shipping_address')
        state = request.POST.get('c_state_country')
        pin = request.POST.get('c_postal_zip')
        email = request.POST.get('c_email')
        mobile = request.POST.get('c_phone')
        total = request.POST.get('c_total')
        message = request.POST.get('c_order_notes')
        obj = OrderDb(Name=name, Email=email, Address=address, ShippingAddress=ship_address, Mobile=mobile, state=state,
                      Pin=pin, TotalPrice=total, Message=message)
        obj.save()
        return redirect(payment)


def payment(request):
    # Retrieve the data from OrderDb with the specified ID
    customer = OrderDb.objects.order_by('-id').first()

    # Get the amount of the specified customer
    payy = customer.TotalPrice

    # convert the amount into paisa ( smallest currency unit )
    # Assuming the payment amount in rupees
    amount = int(payy * 100)

    payy_str = str(amount)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('your_key_id', 'your_key_secret'))

        payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str})


def about(request):
    try:
        cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    except:
        cart_count = None
    return render(request, "about.html", {'cart_count': cart_count})


def contact(request):
    cart_count = CartDb.objects.filter(Username=request.session['username']).count()
    return render(request, "contact.html", {'cart_count': cart_count})


def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        address = request.POST.get('address')
        obj = ContactDb(Name=na, Email=em, Mobile=mob, Address=address)
        obj.save()
        return redirect(display_shop)


# design section
def homepage(request):
    return render(request, "design/category.html")
