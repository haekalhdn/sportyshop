from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoe', 'Sepatu'),
        ('pants', 'Celana'),
        ('shirt', 'Kaos / Training Top'),
        ('outer', 'Jaket / Hoodie'),
        ('socks', 'Kaos Kaki'),
        ('bag', 'Tas Olahraga'),
        ('equipment', 'Perlengkapan (bola, raket, dll)'),
        ('accessory', 'Aksesori (topi, wristband, dll)'),
        ('protection', 'Pelindung (shin guard, dll)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField()
    product_views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name
        
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()