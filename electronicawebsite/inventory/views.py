from django.shortcuts import render
from .models import Product, Supplier, ProductInstance, Category
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()
    num_instances = ProductInstance.objects.all().count()

    # Available products (status = 'a')
    num_instances_available = ProductInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_suppliers = Supplier.objects.count()

    context = {
        'num_products': num_products,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_suppliers': num_suppliers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 2


class ProductDetailView(generic.DetailView):
    model = Product
