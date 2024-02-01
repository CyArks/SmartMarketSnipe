from ResaleValueCalculator import get_average_market_price
from Offer import Offer


class ProductReseller:
    def __init__(self, boughtOffer: Offer):
        print(f"Creating a offer for {boughtOffer.title} which was bought for {boughtOffer.price}")
        self.price = input("Wunsch Preis?")


