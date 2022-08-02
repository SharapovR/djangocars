from django.db import models


class Cars(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cars')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarsShots(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="shots")
    image = models.ImageField(upload_to='carsshots')

    def __str__(self):
        return self.cars.title


class Callback(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
