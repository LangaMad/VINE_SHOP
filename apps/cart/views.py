from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Cart, CartItem

class CartActionView(View):
    def get(self, request, action, item_id):
        if action == 'add':
            return self.cart_add(request, item_id)
        elif action == 'remove':
            return self.cart_remove(request, item_id)
        else:
            # Обработка неподдерживаемых действий, например, вы можете вернуть 404
            return render(request, '404.html')

    def cart_add(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('ProductListView')

    def cart_remove(self, request, cart_item_id):
        cart_item = CartItem.objects.get(pk=cart_item_id)
        cart_item.delete()
        return redirect('CartActionView')

