from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    shortdescription = models.CharField(max_length=300)
    pricepernight = models.CharField(max_length = 30)
    longdescription = models.CharField(max_length=1000)
    amenities = models.CharField(max_length=300)
    detailedimage = models.ImageField(default = None)
    xcoordinate = models.FloatField(default = None, max_length = 30)
    ycoordinate = models.FloatField(default = None, max_length = 30)

    def __str__(self):
      return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()
    guests = models.IntegerField(default =  0)
    preferences = models.CharField(max_length = 500, default = "None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
      return self.listing.title

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   gender = models.CharField(default = "Unspecified", max_length = 20)
   picture = models.ImageField(default = None)

   def __str__(self):
      return self.user.username