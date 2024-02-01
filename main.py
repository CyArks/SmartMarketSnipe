from WillhabenDealsFetcher import Fetcher, SortCrit


myDeals = Fetcher(200, "elektronik", 500, 0, 5020)
myDeals.fetch_offers(20)

for offer in myDeals.fetchedOffers:
    offer.pprint()
