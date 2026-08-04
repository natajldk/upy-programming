class ShoppingCart:
    def __init__(self):
        self.prices=[]
        
    def add(self,prices):
        self.prices.append(prices)
        
    def total(self):
        total=0
        for n in self.prices:
            total=total+n
        return total

cart=ShoppingCart()
for prices in [50,30,20]:
    cart.add(prices)
print(cart.total())