from django.db import models
from django . urls import reverse

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=300,blank=True)
    Cat_image=models.ImageField(upload_to='photos/categories',blank=True)
    is_available=models.BooleanField(default=True)
    category_offer = models.IntegerField(default=0)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
        
    
    # function for catogory slug links
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name
    