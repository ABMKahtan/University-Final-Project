from django.shortcuts import render

def createItem(request):
    print("\nRequest LOGGING: \n", request)
    item = request.POST['item']
    units = request.POST['units']
    ppu_Buy = request.POST['ppu_Buy']
