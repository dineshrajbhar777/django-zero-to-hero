from django.db import models

# Create a custom manager

class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def expensive(self, threshold=1000):
        return self.get_queryset().filter(price__gt=threshold)


# Define your model

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # The default manager
    objects = models.Manager()  

    # Custom manager
    active = ActiveProductManager() 