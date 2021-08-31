from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51JUN7bKa13T77VZLl7hcE9CgX2Aul3YVwxlKeO1Ph0H5rA3jY8QrHDJOkf9UWozeHUWz2aZfCyk31z5O1Kp1UdYt00aQTaTkRM',
        'client_secret' : 'test client secret',
    }


    return render(request, template, context)