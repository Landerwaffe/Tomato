from django.db import models
# Create your models here.
class Listing(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30)
    shortdescription = models.CharField(max_length=300)
    pricepernight = models.CharField(max_length = 30)
    longdescription = models.CharField(max_length=1000)
    amenities = models.CharField(max_length=300)

    def __str__(self):
      return self.title

class Booking(models.Model):
    date = models.DateTimeField(auto_now_add=True)
