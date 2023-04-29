#class attribute is an attribute that belongs to the class itself but however it can also be assessed from the instance level as well

class Item:
    #instantiating class attribute
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validation first
        assert price >=0
        assert quantity >= 0
        
        #assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #actions to execute
        Item.all.append(self) #in the list of all we are appending self. Self is being appended to append each of the instance in the objects
            
    
    #A function that calculates the total price
    def calculate_price(self):
        return self.price * self.quantity
    
    #defining method 
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    #to check list all the items clearly with names mentioned we use __repr__ magic method   
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item_1 = Item('Phone', 20000, 2)

#accessing class attribute
item_1.apply_discount()
#print(item_1.price)

item_2 = Item('Laptop', 30000, 1)
item_2.pay_rate = 0.5 #if to make any changes, make it in local level and not global because it will affect others as well
item_2.apply_discount()
#print(item_2.price) # it will still apply 20 percent discount just because of Item.pay_rate on line:22


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all) #to list all the items

#to print names for each list item
for instance in Item.all:
    print(instance.name)
