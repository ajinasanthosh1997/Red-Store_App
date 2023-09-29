from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name= models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    SIZE_CHOICES=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large')
    )
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    product_details = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    image1 = models.ImageField(upload_to='items_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='items_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='items_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='items_images', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=120,choices=SIZE_CHOICES,default='M')
    tax=models.IntegerField(default=50)

    
    def __str__(self):
        return self.name
    
# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.product.name}"