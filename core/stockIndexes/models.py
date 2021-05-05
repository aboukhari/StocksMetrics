from django.db import models

# Create your models here.

class StocksList(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    fiftyTwoHigh = models.FloatField()
    closing = models.FloatField()
    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(StocksList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
