from django.shortcuts import render,HttpResponse
from home.models import Contact,Deliver,Menu
from django.contrib import messages

def index(request):
    # messages.success(request,"this is my index page")
    return render(request, "index.html")  
def menu(request):
    return render(request,"menu.html")
def cart(request):
    return render(request,"cart.html")
def orderonline(request):
    return render(request,"orderonline.html")
def aboutus(request):
    return render(request,"aboutus.html")
def contactus(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        contact=Contact(name=name ,email=email)
        contact.save()
        messages.success(request, "your response has been sent!!thanks!.")
    return render(request,"contactus.html")
from django.shortcuts import redirect

def deliveron(request):
    if request.method == "POST":#"If the user submitted a form (not just opened the page), then run the below code to save the data."
        # "GET" – when the page is first loaded or data is being fetched
        # "POST" – when a form is submitted to send data (like a contact form or order)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        add = request.POST.get('add')
        de = Deliver(name=name, phone=phone, email=email, add=add)
        de.save()
        messages.success(request, "Your address has been added.")
        return redirect('menu')  # f your add a form then you to do this 
    return render(request, "menu.html")
def menu(request):#here we are just fetching data
    items=Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': items})
# def add_to_cart(request, item_id):
   
#     return redirect('menu')  # or wherever you want

#for cart calculations
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu  # Your item model
from django.views.decorators.csrf import csrf_exempt

def add_to_cart(request, item_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})  # default to empty dict

        # If cart is a list by mistake, convert to dict
        if isinstance(cart, list):
            cart = {item: 1 for item in cart}

        # Increment quantity or set to 1
        if item_id in cart:
            cart[item_id] += 1
        else:
            cart[item_id] = 1
        messages.success(request, "Added to Cart succesfully!!")
        # Save back to session
        request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER', 'menu'))  # or wherever you want to redirect after a



def check(request):
    cart = request.session.get('cart', {})
    items = []
    subtotal = 0

    for item_id, qty in cart.items():
        try:
            item = Menu.objects.get(pk=item_id)
            total_price = item.price * qty
            items.append({
                'item': item,
                'quantity': qty,
                'total_price': total_price
            })
            subtotal += total_price
        except Menu.DoesNotExist:
            continue

    delivery = 40  # flat charge
    grand_total = subtotal + delivery

    return render(request, 'checkout.html', {
        'items': items,
        'subtotal': subtotal,
        'delivery': delivery,
        'grand_total': grand_total,
        'estimated_time': '30-45 minutes',
    })


def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if item_id in cart:
            del cart[item_id]
        request.session['cart'] = cart
    return redirect('cart')

def update_quantity(request, item_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart = request.session.get('cart', {})
        if item_id in cart:
            if action == 'increase':
                cart[item_id] += 1
            elif action == 'decrease':
                cart[item_id] = max(1, cart[item_id] - 1)
        request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    items = Menu.objects.filter(id__in=cart.keys())
    cart_items = []
    subtotal = 0

    for item in items:
        quantity = cart[str(item.id)]
        total_price = item.price * quantity
        subtotal += total_price
        cart_items.append({
            'item': item,
            'quantity': quantity,
            'total_price': total_price
        })

    delivery = 50 if cart_items else 0
    grand_total = subtotal + delivery

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery': delivery,
        'grand_total': grand_total
    })
def view_menu(request):
    items = Menu.objects.all()
    return render(request, 'view.html', {'menu_items': items})
# from django.shortcuts import redirect

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('menu')  # 'menu' should be the name of your menu URL pattern


