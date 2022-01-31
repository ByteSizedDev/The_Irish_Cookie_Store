from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Flavour, Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for entry in bag:
        product = get_object_or_404(Product, pk=entry.get("item_id", None))
        flavours = entry.get("flavours", None)
        quantity = entry.get("quantity", None)

        total += int(quantity) * product.price
        product_count += int(quantity)

        flavours_data = []
        for key in flavours.keys():
            flavour = get_object_or_404(Flavour, pk=key)
            _quantity = flavours.get(key, None)
            flavours_data.append({
                "flavour": flavour,
                "quantity": _quantity
            })

        bag_items.append({
            'item_id': product.id,
            'quantity': int(quantity),
            'product': product,
            'flavours': flavours_data,
        })
        # if isinstance(item_data, int):
        #     total += item_data * product.price
        #     product_count += item_data
        #     bag_items.append({
        #         'item_id': item_id,
        #         'quantity': item_data,
        #         'product': product,
        #     })
        # else:
        #     product = get_object_or_404(Product, pk=item_id)
        #     for size, quantity in item_data.get('items_by_size', {}).items():
        #         total += quantity * product.price
        #         product_count += quantity
        #         bag_items.append({
        #             'item_id': item_id,
        #             'quantity': quantity,
        #             'product': product,
        #             'size': size,
        #         })

    delivery = 6
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context