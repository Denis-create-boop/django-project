from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.views.decorators.http import require_POST
from .catalog import CATEGORIES, product_model

def lookup(category, pk):
    if category not in CATEGORIES:
        raise Http404
    return get_object_or_404(product_model(category), pk=pk)

@require_POST
def add(request, category, pk):
    product = lookup(category, pk)
    if product.price is not None:
        cart = request.session.get('cart', {})
        key = f'{category}:{pk}'
        cart[key] = min(99, cart.get(key, 0) + 1)
        request.session['cart'] = cart
    return redirect('cart')

@require_POST
def change(request, category, pk):
    cart = request.session.get('cart', {})
    key = f'{category}:{pk}'
    if key in cart:
        action = request.POST.get('action')
        if action == 'remove':
            cart.pop(key)
        elif action == 'plus':
            cart[key] = min(99, cart[key]+1)
        elif action == 'minus':
            cart[key] -= 1
            if cart[key] <= 0:
                cart.pop(key)
    request.session['cart'] = cart
    return redirect('cart')

def view(request):
    cart = request.session.get('cart', {})
    rows = []
    total = Decimal('0')
    cleaned = {}
    for key, quantity in cart.items():
        category, pk = key.split(':', 1)
        if category not in CATEGORIES:
            continue
        product = product_model(category).objects.prefetch_related('images').filter(pk=pk).first()
        if not product or product.price is None:
            continue
        subtotal = product.final_price * quantity
        total += subtotal
        cleaned[key] = quantity
        rows.append({'product':product,'category':category,'quantity':quantity,'subtotal':subtotal,'detail_url':CATEGORIES[category]['prefix']+'-detail'})
    if cleaned != cart:
        request.session['cart'] = cleaned
    return render(request, 'main/cart.html', {'rows':rows,'total':total})

def count(request):
    return {'cart_count':sum(request.session.get('cart', {}).values())}
