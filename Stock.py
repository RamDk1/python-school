

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    
    def get_description(self):
        return print(f"{self.ticker}: {self.company} -- ${self.price}")
    
ticker = "GOOG"
price = 185.43
company = "Google LLC"

symbol = Stock(ticker, price, company)
description = symbol.get_description()