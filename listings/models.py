from django.db import models
from django.shortcuts import render, redirect  
from CRUD.forms import PortfolioForm  
from CRUD.models import Portfolio 
import requests

class Listing(models.Model):
    realtor  = models.ForeignKey(Portfolio, on_delete=models.DO_NOTHING)

class Personaldb(models.Model):
    item = models.CharField(max_length=50)
    units_owned = models.IntegerField()
    ppu_buy = models.FloatField()
    # ppu_sell = models.FloatField()
    # current_profit = models.FloatField()
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

