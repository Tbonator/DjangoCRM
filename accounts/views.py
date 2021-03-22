from accounts.models import Customers, Order, Product
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.forms import inlineformset_factory
from .forms import OrderForm

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


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customers, Order, fields=('product', 'status'))
    customer = Customers.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        #form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, "accounts/order_form.html", context)


def updaterOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = OrderForm(instance=order)
    context = {'form': form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
