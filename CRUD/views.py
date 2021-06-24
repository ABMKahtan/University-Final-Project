from django.shortcuts import render, redirect  
from CRUD.forms import PortfolioForm  
from CRUD.models import Portfolio 
from django.contrib import messages, auth
import requests

# Create your views here.  

def emp(request):  
    if request.method == "POST":  
        form = PortfolioForm(request.POST)  

        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/editdb/show/')  
            except:  
                pass  
    else:  
        form = PortfolioForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    portfolios = Portfolio.objects.all()  
    return render(request,"show.html",{'portfolios':portfolios})  

def edit(request, id):  
    portfolio = Portfolio.objects.get(id=id)  
    return render(request,'edit.html', {'portfolio':portfolio})  

def update(request, id):  
    portfolio = Portfolio.objects.get(id=id)  
    form = PortfolioForm(request.POST, instance = portfolio)  
    if form.is_valid():  
        form.save()  
        return redirect("editdb/show")  
    return render(request, 'edit.html', {'portfolio': portfolio})  

def destroy(request, id):  
    portfolio = Portfolio.objects.get(id=id)  
    portfolio.delete()
    messages.success(request, 'Item Has Been Deleted')
    return redirect("/about")  

def finance(request): 
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete?q=takeaway&region=UK' 
    headers = {
        "x-rapidapi-key": "04ba50d588msh5b584e8242c3366p1b8248jsn07bb88bb52a7",
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
        "useQueryString": "true"
    }
    response = requests.get(url, headers=headers)

    financedata = response.json()
    return render(request, 'index.html', {
        'abilities': financedata['quotes']
    })