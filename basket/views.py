from django.shortcuts import render, redirect, get_object_or_404

from library.models import book
from .basket import Basket
from .forms import BasketAddProductForm
from django.views.decorators.http import require_POST


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(book, pk=product_id)
    form = BasketAddProductForm(request.POST)

    if form.is_valid():
        basket.add(product=product_obj, count_product=form.cleaned_data['count_prod'],
                   update_count=form.cleaned_data['update'])
    return redirect('list_basket_prod')


def basket_remove(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(book, pk=product_id)
    basket.remove(product=product_obj)
    return redirect('list_basket_prod')

def basket_info(request):
    basket = Basket(request)
    for item in basket:
        item['update_count_form'] = BasketAddProductForm(initial={'count_prod': item['count_prod'], 'update': True})
    return render(request, 'basket/cart.html', {'basket': basket})

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('index')