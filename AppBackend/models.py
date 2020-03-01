from django.db import models

address_choices = (
    ("Ramanujan", "Ramanujan"),
    ("Bhabha", "Bhabha"),
    ("Raman", "Raman"),
    ("Bose", "Bose"),
)

# Create your models here.


class RentSomething(models.Model):
    name = models.CharField(max_length=256)
    SellerName = models.CharField(max_length=256)
    image = models.ImageField(null=False, blank=False)
    cost = models.CharField(max_length=4)
    address = models.CharField(
        max_length=20, choices=address_choices, default='Ramanujan')
    roomNum = models.CharField(max_length=3)
    mobileNum = models.CharField(max_length=10)

    def __str__(self):
        return self.name+","+self.SellerName