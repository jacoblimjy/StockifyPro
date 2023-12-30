from django.db import models
from django import forms

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
    

class StockForm(forms.ModelForm):
    # Meta class is used to tell Django which model should be used to create this form (model = Stock)
    class Meta:  
        model = Stock
        fields = ["ticker"]

