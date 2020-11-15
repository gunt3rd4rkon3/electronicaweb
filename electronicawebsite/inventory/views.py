from django.shortcuts import render
from .models import Product, Supplier, ProductInstance, Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import OrderProductForm


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
    paginate_by = 20


class ProductDetailView(generic.DetailView):
    model = Product


class SupplierListView(generic.ListView):
    model = Supplier
    paginate_by = 20


class SupplierDetailView(generic.DetailView):
    model = Supplier


class BoughtProductsByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing products buyed by the current user"""
    model = ProductInstance
    template_name = 'inventory/productinstance_list_sinnombre_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ProductInstance.objects.filter(sinnombre=self.request.user).filter(status__exact='a').order_by('available_date')


class LoanedProductsAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based  view listing products on loan to current user"""
    model = ProductInstance
    permission_required = 'inventory.can_mark_returned'
    template_name = 'inventory/productinstance_list_available_all.html'
    paginate_by = 10

    def get_queryset(self):
        return ProductInstance.objects.filter(status__exact='a').order_by('available_date')


@login_required
@permission_required('inventory.can_mark_returned', raise_exception=True)
def order_product_worker(request, pk):
    """View function for order a specific ProductInstance by worker"""
    product_instance = get_object_or_404(ProductInstance, pk=pk)

    # if this is a POST request then process the form data
    if request.method == 'POST':

        # create a form instance and postulate it with data form the request (binding):
        form = OrderProductForm(request.POST)

        # check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model available_date field)
            product_instance.available_date = form.cleaned_data['order_date']
            product_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-available'))

    # if this is a GET ( or any other method ) create the default form
    else:
            proposed_landing_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = OrderProductForm(initial={'available_date': proposed_landing_date})

    context = {
            'form': form,
            'product_instance': product_instance,
    }

    return render(request, 'inventory/product_order_worker.html', context)


class SupplierCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'inventory.can_mark_returned'
    model = Supplier
    fields = ['business_name', 'business_email', 'cif']


class SupplierUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'inventory.can_mark_returned'
    model = Supplier
    fields = '__all__'


class SupplierDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'inventory.can_mark_returned'
    model = Supplier
    success_url = reverse_lazy('suppliers')


class ProductCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'inventory.can_mark_returned'
    model = Product
    fields = ['title', 'supplier', 'maxunits', 'stock', 'summary', 'sn', 'category']


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'inventory.can_mark_returned'
    model = Product
    fields = '__all__'


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'inventory.can_mark_returned'
    model = Product
    success_url = reverse_lazy('products')
