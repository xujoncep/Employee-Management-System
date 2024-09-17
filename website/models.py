from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=50)
    description = models.TextField(default="No description available")


    def __str__(self):
        return self.name