from django.db import models

# Create your models here.
from django.urls import reverse

from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    class Meta:
        verbose_name_plural = 'Products'
