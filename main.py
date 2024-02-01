from DealsFetcher import Fetcher, SortCrit, FilterCrit
from ResaleValueCalculator import ResaleValueCalculator

myDeals = Fetcher(200, "elektronik", 500, 0, 5020)
myDeals.fetch_offers(20)

for offer in myDeals.fetchedOffers:
    offer.pprint()


# Assuming fetchedOffers is a list of Offer objects
calculator = ResaleValueCalculator(myDeals.fetchedOffers)
sorted_offers_by_potential_gain = calculator.analyze_offers()

