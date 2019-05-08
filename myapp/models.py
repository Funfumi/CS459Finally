from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.id}_{self.name}'