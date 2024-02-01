import time
import pandas
import requests
from Offer import Offer
from bs4 import BeautifulSoup


class SortCrit:
    PriceMaxToMin = "max_to_min"
    PriceMinToMax = "min_to_max"
    DistanceMinToMax = "dist_min_to_max"
    DistanceMaxToMin = "dist_max_to_min"
    conditionGoodToBad = "cond_good_to_bad"


class FilterCrit:
    condition = "condition"
    price = "price"
    postalCode = "post_code"
    maxDistance = "max_distance"


class Fetcher:
    def __init__(self, max_distance, category, max_price=None, min_price=None, postcode=None):
        self.max_distance = max_distance
        self.max_price = max_price
        self.min_price = min_price
        self.category = category
        self.postcode = postcode

        self.fetchUrl = f"https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/{category}-{postcode}"
        self.fetchedOffers = []

    def sort_fetched_offers(self, sortCrit: SortCrit = SortCrit.PriceMinToMax):
        pass

    def filter_offers(self, filterCrit: FilterCrit = FilterCrit.price, filterDirection="DESC"):
        pass

    def fetch_offers(self, quantity):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}

        # Headers:
        # Filter: Box-sc-wfmb7k-0 fTcRCp - class

        response = requests.get(self.fetchUrl, headers=headers)

        if response.status_code == 200:
            # Pars response to html and throw away unnecessary stuff
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find('div', class_='Box-sc-wfmb7k-0 sc-bf4f682c-0 ccoBUA jqBjhX')
            offerList = soup.find_all('div', class_='Box-sc-wfmb7k-0 hzLKyY')

            for offer in offerList:
                # Extract data from listings
                title = offer.find('h3', class_='Text-sc-10o2fdq-0 jAfyki').text.strip()
                price = offer.find('div', class_='Box-sc-wfmb7k-0 dUrVmT').text
                location = offer.find('span', class_='Text-sc-10o2fdq-0 bFMMYK').text
                pTime = offer.find('p', class_='Text-sc-10o2fdq-0 dvUlKL').text
                condition = offer.find()  # ToDo
                postalCode = offer.find()  # ToDo
                vendorName = offer.find()  # ToDo
                pDate = offer.find()  # ToDo
                imageUrl = offer.find()  # ToDo

                newOffer = Offer(title, self.category, price, condition, postalCode, location, vendorName, pDate, pTime,
                                 self.fetchUrl, imageUrl)
                self.fetchedOffers.append(newOffer)

            print(f"Successfully fetched {self.fetchedOffers.__len__()} offer/s")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
