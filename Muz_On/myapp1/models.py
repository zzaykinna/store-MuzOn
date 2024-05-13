from django.db import models
class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length = 35, blank = False)
    last_name = models.CharField(max_length = 35, blank = False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name}'

class About(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length = 350, blank = False)

    def __str__(self):
        return f'{self.name} {self.description}'
class Catalog(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length = 350, blank = False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'