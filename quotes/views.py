from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
import requests
import json

PUBLICKEY = "pk_ae8477a1bf7d4b6ca8c14bb9a2476c1b"


# Create your views here.
def Home(request):
    
    if request.method == 'POST':
        ticker = request.POST['ticker']
        urllit = "https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token="+PUBLICKEY
        api_request = requests.get(urllit)

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

def AddStock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock Has Been Added!'))
            return redirect('add_stock')
    else:
        ticker =  Stock.objects.all()
        output = []
        for ticker_item in ticker:

            urllit = "https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) +"/quote?token="+PUBLICKEY
            api_request = requests.get(urllit)

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def DeleteStock(request):
        ticker =  Stock.objects.all()
        return render(request, 'delete_stock.html', {"ticker":ticker})


def About(request):
    return render(request, 'about.html', {})

def Delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(DeleteStock)