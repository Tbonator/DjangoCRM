from accounts.models import Customers, Order, Product
from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customers.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {'products': products})
#  whatever is the key is in the dictionary what is called in template


def customer(request, pk):
    # fetching individual customer using pk
    customer = Customers.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count

    }
    return render(request, "accounts/customer.html", context)
