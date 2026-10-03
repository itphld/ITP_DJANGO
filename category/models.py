from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50)
    description=models.TextField()
    cat_image=models.ImageField(upload_to='category/')
    is_active=models.BooleanField(default=True)
    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name
