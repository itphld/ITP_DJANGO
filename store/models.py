from django.db import models
from category.models import Category
from django.urls import reverse
class Product(models.Model):
    product_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50)
    description=models.TextField()
    stock=models.IntegerField()
    price=models.DecimalField(decimal_places=      2,max_digits=10)
    product_image=models.ImageField(upload_to='Product/')
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

# Create your models here.
