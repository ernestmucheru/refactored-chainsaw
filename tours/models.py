from django.db import models

# Create your models here.
class Tour(models.Model):

    id = models.IntegerField(primary_key=True)
    tour = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=400)
    photos = models.ImageField(upload_to='img')
    blog = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tour