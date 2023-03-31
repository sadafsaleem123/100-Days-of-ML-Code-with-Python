class Item:
    def __init__(self, name: str, price: float, quantity=0):
        #Run validation first
        assert price >=0
        assert quantity >= 0
        
        #assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity
    
    #a function that calculates the total price
    def calculate_price(self):
        return self.price * self.quantity

item_1 = Item('Phone', 1000, 2)
item_2 = Item('Laptop', 30000, 1)

print(item_1.calculate_price())
print(item_2.calculate_price())

#Here assert will only print those items that validates the statement otherwise if the condition doesn't meet it will throw a ValidationError!

