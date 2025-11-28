from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self,price):
        self.price = price 
    
    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company
    
    def get_description(self):
        return f"{self.ticker}: {self.company} --  ${self.price}"


class Bond(Asset):
    def __init__(self, price, duration, description, interest):
        super().__init__(price)
        self.duration = duration
        self.description = description
        self.interest = interest
    
    def get_description(self):
        return f"{self.description}: {self.duration} : ${self.price} : {self.interest}"

ticker = "MSFT"
price = 400.00
description = "Microsoft Corporation"
bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38


stock = Stock(ticker, price, description)
stock_description = stock.get_description()

bond = Bond(bondprice, bondname, duration, interest)
bond_description = bond.get_description()

print(bond_description)
print(stock_description)
