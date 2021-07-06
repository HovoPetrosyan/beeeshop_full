from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)
    image = models.ImageField(upload_to='photos/categories', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

    class Meta:
        verbose_name_plural = 'Categories'
