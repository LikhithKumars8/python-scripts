from django.db import models

class SalesData(models.Model):
    REGION_CHOICES = [
        ('A', 'Region A'),
        ('B', 'Region B'),
    ]

    order_id = models.CharField(max_length=50, unique=True)
    batch_id = models.CharField(max_length=10, blank=True, null=True)
    order_item_id = models.CharField(max_length=50)
    quantity_ordered = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    region = models.CharField(max_length=1, choices=REGION_CHOICES)
    net_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_id} - Item {self.order_item_id} (Region: {self.region})"

class Jokes(models.Model):
    category = models.CharField(max_length=100, blank=True)
    joke_type = models.CharField(max_length=10, blank=True)
    joke = models.TextField(blank=True, default="")
    setup = models.TextField(blank=True, default="")
    delivery = models.TextField(blank=True, default="")
    nsfw = models.BooleanField(default=False)
    political = models.BooleanField(default=False)
    sexist = models.BooleanField(default=False)
    safe = models.BooleanField(default=True)
    lang = models.CharField(max_length=10, default="en")

    def __str__(self):
        return f"{self.joke[:50]} - {self.category}"