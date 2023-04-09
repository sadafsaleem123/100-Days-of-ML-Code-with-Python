#class attribute is an attribute that belongs to the class itself but however it can also be assessed from the instance level as well

class Item:
    #instantiating class attribute
    pay_rate = 0.8
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

#accessing class attribute
print(Item.pay_rate)

#accessing instance attribute
print(item_1.pay_rate)
print(item_2.pay_rate)
# this will access the attribute in instance level first, and because it doesn't find any attribute at this level it shows the result for global level attribute

#To find all the attributes belonging to a specific object we use __dict__ 
print(Item.__dict__) #All the attributes for class level
print(item_1.__dict__) #All the instance for class level

