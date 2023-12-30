from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import requests
import json
from .models import Stock, StockForm
from django.contrib import messages


# Create your views here.
# def home(request):
#     if request.method == 'POST':
#         ticker = request.POST['ticker']
#         #api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/<ticker>?token=<your token>")
#         api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/" + ticker + "?token=pk_7fdc1579fa064fdabb11bc01622ff78d")
#         try:
#             api = json.loads(api_request.content)
#         except Exception as e:
#             api = "Error..."
#         return render(request, 'about.html', {'api': api})
#     else:
#         return render(request, 'about.html', {'ticker': "Enter a ticker symbol above..."})

def search_stock(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        #api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/<ticker>?token=<your token>")
        api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/" + ticker + "?token=pk_23492b2c700d47c8a71103ad3044ed19")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'search_stock.html', {'api': api})
    else:
        return render(request, 'search_stock.html', {'ticker': "Enter a ticker symbol above..."})
    
def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added!")) 
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            try:
                api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/" + ticker_item.ticker + "?token=pk_23492b2c700d47c8a71103ad3044ed19")
                api = json.loads(api_request.content)
                api[0]["id"] = ticker_item.id
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted!"))
    return redirect(add_stock)

#I am using newsapi.org for the news section of the website.
def getTopNews(request): #Get the top news from the API
    # Replace 'YOUR_API_KEY' with your actual News API key
    news_api_key = '359aeb93a99b4162a6d086d55db94d26'
    # Get business news
    news_api_url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={news_api_key}'

    try:
        response = requests.get(news_api_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            news_data = response.json()
            articles = news_data.get('articles', [])
            return render(request, 'news.html', {'articles': articles})
        else:
            # If the request was not successful, handle the error
            messages.error(request, "Failed to fetch top news.")
    except Exception as e:
        # Handle any exceptions that may occur during the request
        messages.error(request, f"An error occurred: {str(e)}")
    # If there was an error, or no articles were retrieved, return an empty list
    return render(request, 'news.html', {'articles': []})

from datetime import date, timedelta

def getNews(request):
    news_api_key = '359aeb93a99b4162a6d086d55db94d26'

    if request.method == 'POST':
        query = request.POST.get('query', '')
        
        # from_date = (date.today() - timedelta(days=1)).isoformat()

        news_api_url = f'https://newsapi.org/v2/everything?q={query}&from=2023-12-20&sortBy=popularity&apiKey={news_api_key}'
        try:
            response = requests.get(news_api_url)
            if response.status_code == 200:
                news_data = response.json()
                articles = news_data.get('articles', [])
                return render(request, 'search_news.html', {'articles': articles, 'query': query})
            else:
                messages.error(request, "Failed to fetch news.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")  # Add this line for debugging
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, 'search_news.html', {'articles': [], 'query': ''})
