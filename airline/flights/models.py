# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 6:36:08
# We define what models exist for our app. Every model is a Python class, one model per every table we care to store information about.

from django.db import models

# Create your models here.
# Create the Airport class. - 6:44:31
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # Adjust the origin and destination to reference the Airport class as a Foreign key. - 6:45:00
    # models.CASCADE says that if I delete any data in the table that is being referenced, the referencing object also gets deleted. - 6:46:08
    # models.PROTECT will prevent deletion of data if references to that data still exist. 
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # Any model can implement __str__ function which represents a string representation of that particular object. Applies to Django models and Python classes. - 6:42:36
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"