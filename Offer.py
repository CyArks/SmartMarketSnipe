from pprint import pprint


class Offer:
    def __init__(self, title, category, price, condition, postalCode, location, vendorName, pDate, pTime, url, imageUrl):
        self.title = title
        self.category = category
        self.price = price
        self.condition = condition
        self.postalCode = postalCode
        self.location = location
        self.vendorName = vendorName
        self.publishDate = pDate
        self.publishTime = pTime
        self.url = url
        self.imageUrl = imageUrl

    def send_message(self):
        pass

    def send_buy_req(self):
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

    def createOffer(self):
        pass

