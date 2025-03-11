from django.db import transaction
from django.db.models import Prefetch, Sum
from django.shortcuts import redirect, render
from django.utils import timezone

from core.forms import ProductOrderForm

from .models import Restaurant, Sale


# Create your views here.
def index(request):
    # Get all 5-stars ratings, and fetch all the sales for restaurants with 5-star rating.
    # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales') \
    #     .filter(ratings__rating=5) \
    #     .annotate(total=Sum('sales__income'))

    # Get all 5-stars ratings, and fetch all the sales for restaurants on the last month.
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch('sales', queryset=Sale.objects.filter(datetime__gte=month_ago))
    restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5)
    restaurants = restaurants.annotate(total=Sum('sales__income'))
    print([res.total for res in restaurants])
    return render(request, 'index.html')


def order_product(request):
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():

            with transaction.atomic():
                order = form.save()
                order.product.number_in_stock -= order.number_of_items
                order.product.save()
            transaction.on_commit(lambda: print(f'Order committed'))
            return redirect('order-product')
        else:
            context = {'form': form}
            return render(request, 'order.html', context)

    form = ProductOrderForm()
    context = {'form': form}
    return render(request, 'order.html', context)
