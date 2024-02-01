import os
import time
import requests
from Cache import PriceCache
from bs4 import BeautifulSoup


def get_average_market_price(productName, condition_score):
    """Get the average market price for a product """
    cache = PriceCache()
    cache_key = f"{productName}_{condition_score}"
    cached_price = cache.get(cache_key)

    # Construct the search URL for a marketplace
    # ToDo: Add different market places or call an API
    # ToDo: Add currency + umrechnung + currency_risk
    search_url = f"https://example-marketplace.com/search?q={productName.replace(' ', '+')}"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find elements containing price information
    prices = []
    for price_tag in soup.find_all('span', class_='price-class'):
        price = float(price_tag.text.replace('$', ''))
        prices.append(price)

    if prices:
        return sum(prices) / len(prices)
    else:
        return 0
