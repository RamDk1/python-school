class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    
    def __eq__(self,value):
        if not isinstance(value,Stock):
            raise ValueError("Can't compare a non-Stock.")
        return self.price == value.price
    
    def __gt__(self,value):
        if not isinstance(value,Stock):
            raise ValueError("Can't compare a non-Stock.")
        return self.price > value.price
    
    def __lt__(self,value):
        if not isinstance(value,Stock):
            raise ValueError("Can't compare a non-Stock.")
        return self.price < value.price
    
    def __ge__(self,value):
        if not isinstance(value,Stock):
            raise ValueError("Can't compare a non-Stock.")
        return self.price >= value.price
    
    def __le__(self,value):
        if not isinstance(value,Stock):
            raise ValueError("Can't compare a non-Stock.")
        return self.price <= value.price

ticker1 = "XYZ"
ticker2 = "ABCD"
price1 = 100.0
price2 = 105.1
company1 = "XYZ Corporation"
company2 = "ABCD Company"

stock1 = Stock(ticker1, price1, company1)
stock2 = Stock(ticker2, price2, company2)

is_eq = (stock1 == stock2)
is_gt = (stock1 > stock2)
is_lt = (stock1 < stock2)
is_ge = (stock1 >= stock2)
is_lte = (stock1 <= stock2)

print(is_eq)
print(is_ge)
print(is_gt)
print(is_lt)
print(is_lte)