class Inventory:
    def __init__ (self):
        self.stock={}
    
    def add (self, name, qty):
        self.stock[name]=qty
    
    def low_stock(self, limit):
        low=[]
        for name in self.stock:
            if self.stock[name] < limit:
                low.append(name)
        return low
inv=Inventory()
inv.add("pens",3)
inv.add("pencil",5)
inv.add("eraser",1)
print(inv.low_stock(5))
            