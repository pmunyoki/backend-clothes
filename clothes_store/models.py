from django.db import models

# Create your models here.
class cloth(models.Model):
    type = models.CharField(max_length=1000)
    count = models.IntegerField(default=0)


# create review table with a foreign key referencing the cloth model
