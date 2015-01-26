from django.shortcuts import render, redirect
from models import Product, Order
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.




def cartItems(cart):
    items=[]
    for item in cart:
        # append the actual item to the array
        items.append(Product.objects.get(id=item))
    return items

def genItemsList(cart):
    cart_items=cartItems(cart)
    item_list=""
    for item in cart_items:
        item_list+=str(item.name)
        item_list+=","
    return item_list


def priceCart(cart):
    cart_items=cartItems(cart)
    price=0
    for item in cart_items:
        price+=item.price

    return price



def catalog(request):
    # check cart is empty, if empty, create it.
    if 'cart' not in request.session:
        request.session['cart']=[]
    cart=request.session['cart']
    request.session.set_expiry(0)
    store_items=Product.objects.all()
    ctx={'store_items':store_items,'cart_size':len(cart)}

    if request.method=="POST":
        cart.append( int(request.POST['obj_id'])  )
        return redirect('catalog')

    return render(request,"catalog.html",ctx)


def cart(request):
    cart=request.session['cart']
    request.session.set_expiry(0)
    ctx={'cart':cart,'cart_size':len(cart),'cart_items':cartItems(cart),'total_price': priceCart(cart)}
    return render(request,"cart.html",ctx)


def removefromcart(request):
    request.session.set_expiry(0)
    a=request.POST['obj_id']
    b=""
    for i in a:
        if i!="/":
            b+=i
    obj_to_remove = int(b)
    obj_index=request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(obj_index)
    return redirect('cart')

def checkout(request):
    request.session.set_expiry(0)
    cart=request.session['cart']
    ctx={'cart':cart,'cart_size':len(cart),'total_price':priceCart(cart)}
    return render(request,"checkout.html",ctx)

def completeOrder(request):
    request.session.set_expiry(0)
    cart=request.session['cart']
    order=Order()
    order.first_name=request.POST['firstname']
    order.last_name=request.POST['lastname']
    order.address=request.POST['address']
    order.city=request.POST['city']
    order.payment_method=request.POST['payment']
    order.payment_data=request.POST['payment_data']
    order.items=genItemsList(cart)
    #order.fulfilled=request.POST.get('fulfilled','')
    request.session['cart']=[]
    order.save()
    return render(request,"complete_order.html",None)




def adminLogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("admin")
        else:
            return render(request,"admin_login.html",{'login':False})
    return render(request,"admin_login.html",None)

@login_required
def adminDashboard(request):
    orders=Order.objects.all()
    ctx={'orders':orders}
    return render(request,"admin_panels.html",ctx)







