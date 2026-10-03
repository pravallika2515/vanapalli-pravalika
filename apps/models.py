from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=100)
    quatity=models.IntegerField()
    added_date=models.DateTimeField(auto_now_add=True)