from realtors.views import portfolio
from django.shortcuts import render
from  CRUD import views
from django.db import models
from django.shortcuts import render, redirect  
from CRUD.forms import PortfolioForm  
from CRUD.models import Portfolio
import json
import requests




def index(request):
    return render(request, 'listings/portfolio.html')

def listing(request):
    return render(request, 'listings/listing.html')

# def finance(requests, stockname): # finance(requests, stockname)
#     url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete?q='+ stockname +'&region=UK' 
#     headers = {
#         "x-rapidapi-key": "04ba50d588msh5b584e8242c3366p1b8248jsn07bb88bb52a7",
#         "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
#         "useQueryString": "true"
#     }
#     response = requests.get(url, headers=headers)

#     financedata = response.json()
#     return  financedata

def finance(request, stockname):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region":"US","symbols":stockname}

    headers = {
        'x-rapidapi-key': "60909723c4msh05634bae1edbfe9p1031b0jsn791c1799d71f",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    financedata = response.json()
    return financedata['quoteResponse']['result'][0]['regularMarketPrice']


def show(request):  
    portfolios = Portfolio.objects.all()

    for portfolio in portfolios:
        portfolio.current_price = finance(request,portfolio.item)
        tempUnit = (portfolio.current_price - portfolio.ppu_buy) * portfolio.units_owned
        portfolio.current_profit = "{:.2f}".format(tempUnit)
    return render(request,"listings/portfolio.html",{'portfolios':portfolios}) 

def delete(request, id):  
    return redirect('listings/listing.html')  

def emp(request):  
    if request.method == "POST":  
        form = PortfolioForm(request.POST)  

        if form.is_valid():  
            try:  
                form.save()  
                return redirect('listings/listing.html')  
            except:  
                pass  
    else:  
        form = PortfolioForm()  
    return render(request,'index.html',{'form':form})  