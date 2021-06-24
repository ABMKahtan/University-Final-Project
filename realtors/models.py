from django.db import models

class Portfolio(models.Model):
#if logged in this is personal portfolio ... as of this moment   
    item = models.CharField(max_length=200)
    units_Owned = models.IntegerField(default=0)
    price_Per_Unit_Buy = models.FloatField(default=0)
    price_Per_Unit_Sell = models.FloatField(default=0)
#    A = price_per_Unit_Sell-price_Per_Unit_Buy
#    profit = models.FloatField()
#    profit = A*units_Owned
