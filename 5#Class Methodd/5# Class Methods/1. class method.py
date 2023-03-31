import csv
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
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    #to check list all the items clearly with names mentioned we use __repr__ magic method   
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
