from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    quantity_per_package = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def has_flavours(self):
        try:
            return self.flavours.all().exists()
        except:
            return None

    @property
    def get_flavours(self):
        try:
            return self.flavours.all()
        except:
            return None

class Flavour(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="flavours")
    name = models.CharField(max_length=254)
    description = models.TextField()

    def get_images(self):
        try:
            return self.images.all()
        except:
            return None


class FlavourImage(models.Model):
    parent = models.ForeignKey(Flavour, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(null=True, blank=True)