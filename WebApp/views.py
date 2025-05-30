from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from AdminApp.models import CategoryDb, ProductDb
from WebApp.models import UserRegistrationDb, CartDb, OrderDb, ContactDb, PaymentDetails, OrderTracking
import re
from django.contrib import messages
from django.conf import settings
import razorpay
from django.urls import reverse
from django.http import JsonResponse
import json


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

        # Validate that passwords match
        if ps1 != ps2:
            messages.error(request, "Passwords do not match.")
            return redirect(signup_page)

        # Password Validation: Minimum 8 characters, 1 number, 1 special character, 1 uppercase, and 1 lowercase letter
        if len(ps1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect(signup_page)

        if not re.search(r'[A-Za-z]', ps1) or not re.search(r'[0-9]', ps1) or not re.search(r'[^A-Za-z0-9]', ps1):
            messages.error(request, "Password must contain at least one letter, one number, and one special character.")
            return redirect(signup_page)

        if not any(char.isupper() for char in ps1):
            messages.error(request, "Password must contain at least one uppercase letter.")
            return redirect(signup_page)

        if not any(char.islower() for char in ps1):
            messages.error(request, "Password must contain at least one lowercase letter.")
            return redirect(signup_page)


        # Validate mobile number length
        if len(cont) != 10:
            messages.error(request, "Invalid mobile number")
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


def edit_profile_page(request):
    un = request.session['username']
    data = UserRegistrationDb.objects.get(username=un)
    return render(request, "edit_profile.html", {'data': data})


def update_user(request):
    if request.method == "POST":
        un = request.POST.get('username')
        ps1 = request.POST.get('ps1')
        print(ps1)
        ps2 = request.POST.get('ps2')
        em = request.POST.get('email')
        cont = request.POST.get('contact')

        if ps1 != ps2:
            messages.error(request, "Passwords do not match.")
            return redirect(edit_profile_page)

        # Password Validation: Minimum 8 characters, 1 number, 1 special character, 1 uppercase, and 1 lowercase letter
        if len(ps1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect(edit_profile_page)

        if not re.search(r'[A-Za-z]', ps1) or not re.search(r'[0-9]', ps1) or not re.search(r'[^A-Za-z0-9]', ps1):
            messages.error(request, "Password must contain at least one letter, one number, and one special character.")
            return redirect(edit_profile_page)

        if not any(char.isupper() for char in ps1):
            messages.error(request, "Password must contain at least one uppercase letter.")
            return redirect(edit_profile_page)

        if not any(char.islower() for char in ps1):
            messages.error(request, "Password must contain at least one lowercase letter.")
            return redirect(edit_profile_page)

        # Validate mobile number length
        if len(cont) != 10:
            messages.error(request, "Invalid mobile number")
            return redirect(edit_profile_page)

        UserRegistrationDb.objects.filter(username=un).update(password=ps1, conf_password=ps2, email=em, contact=cont)
        messages.success(request, "Successfully updated profile.")
        return redirect(edit_profile_page)


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
        client = razorpay.Client(auth=('your key id', 'your key secret'))

        payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request, "payment1.html", {'customer': customer, 'payy_str': payy_str})


# View to handle the saving of payment details after successful transaction
def save_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_id = data.get('payment_id')
        order_id = data.get('order_id')
        amount = data.get('amount')
        user_name = data.get('user')
        # print(user_name)

        # Find the order by order_id
        try:
            order = OrderDb.objects.get(id=order_id)
            # Create a PaymentDetails record
            payment_details = PaymentDetails.objects.create(
                order=order,
                user_name=user_name,
                payment_id=payment_id,
                amount=amount,
                status="Success"  # You can set the status as "Success" once payment is verified
            )

            # Create an OrderTracking record for tracking purposes
            OrderTracking.objects.create(
                order=order,
                user_name=user_name,
                payment=payment_details,
                tracking_status="Payment Successful"
            )

            return JsonResponse({'status': 'success'})
        except OrderDb.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Order not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def payment_success(request, order_id):
    try:
        # Get the order and its payment details
        order = OrderDb.objects.get(id=order_id)
        order_tracking = OrderTracking.objects.filter(order=order).first()
        user_name = order_tracking.user_name

        cart_items = CartDb.objects.filter(Username=user_name)
        cart_items.delete()

        if order_tracking:

            return render(request, 'payment_success.html', {'order': order, 'order_tracking': order_tracking})
        else:
            return render(request, 'payment_failed.html', {'order': order})

    except OrderDb.DoesNotExist:
        return render(request, 'payment_failed.html', {'error_message': 'Order not found'})



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
