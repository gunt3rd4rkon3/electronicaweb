from django.db import models
from django.urls import reverse
import uuid  # Required for unique product instance


class Category(models.Model):
    """Model representing a product Category"""
    name = models.CharField(max_length=200, help_text='Enter a product Category (e.g. Motherboard, CPU)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Product(models.Model):
    """Model representing a product (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreing Key used because product can only have one supplier, but suppliers can have multiple products
    # Supplier as a string rather than object because it hasn´t been declare yet in the file
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the product')
    sn = models.CharField('SN', max_length=30, help_text='30 Char MaxSize <a href="https://en.wikipedia.org/wiki/Serial_number">S/N</a>')

    # ManyToManyField used because Category can contain many products ¿?. Products  can cover many categorys¿?.
    # !!! Category class has already been defined so we can specify  the object above. !!!
    category = models.ManyToManyField(Category, help_text='Select a Category for this product')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('product-detail', args=[str(self.id)])


class ProductInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular product across whole inventory')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    register_date = models.DateField(null=True, blank=True)

    PRODUCT_STATE = (
        ('a', 'Available'),
        ('s', 'Sold'),
        ('i', 'Incoming'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=PRODUCT_STATE,
        blank=True,
        default='i',
        help_text='Product availability',
    )

    class Meta:
        ordering = ['register_date']

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.id} ({self.book.title})'


class Supplier(models.Model):
    """Model representing an Supplier."""
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField(max_length=100)
    cif = models.CharField(max_length=9)

    class Meta:
        ordering = ['business_name', 'cif']

    def get_absolute_url(self):
        """Return the url to access a particular supplier instance."""
        return reverse('supplier_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.business_name}, {self.business_email}, {self.cif}'

