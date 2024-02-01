from pprint import pprint
from ImageAnalysisTool import analyze_image
from ResaleValueCalculator import get_average_market_price


class Offer:
    def __init__(self, title, category, price, condition, postalCode, location, vendorName, pDate, pTime, url, imageUrl):
        self.title = title
        self.category = category
        self.price = price
        self.condition = condition
        self.imageUrl = imageUrl
        self.postalCode = postalCode
        self.location = location
        self.vendorName = vendorName
        self.publishDate = pDate
        self.publishTime = pTime
        self.url = url

        self.condition_score = None
        self.avg_market_price = None
        self.potential_gain = None

    def analyze(self):
        self.condition_score = analyze_image(self.imageUrl)
        self.avg_market_price = get_average_market_price(self.title, self.condition_score)
        self.potential_gain = self.avg_market_price - self.price

    def send_message(self):
        # ToDo: Implement a way to send messages -> Account login needed in the first place
        pass

    def send_buy_req(self):
        # ToDo: Use send message function if pay-delivery is not available to auto send a price offer
        pass

    def pprint(self):
        pprint(vars(self))

    def print_offer(self):
        try:
            print(self.title)
            print(self.price)
            print(self.location)
            print(self.publishDate)
            print(self.publishTime)
        except Exception as e:
            print(e)
        finally:
            print("\n\n")

    def get_similar_offers(self):
        # ToDo: Get similar offers based on title and category
        # ToDo: Use google vision to compare and filter results
        pass

