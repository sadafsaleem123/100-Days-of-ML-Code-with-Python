#SET:01

'''
class Item:
    pass

item_1 = Item()
item_1.name = 'Phone'

item_2 = Item()
item_2.name = 'Laptop'

print(item_1)
print(item_2)

#Here we have created an attribute of item_1 and item_2 that is named by item_1.name and item_2.name
#To avoid the creation of attribtes manually, we can create __init__ magic method.


#SET:02

class Item:
    def __init__(self, name):
        self.name = name

item_1 = Item('Phone')
item_2 = Item('Laptop')

print(item_1.name)
print(item_2.name)


#SET:03
#Now to demonstrate the arguments by its types we specify it in class as:
class Item:
    def __init__(self, name: str, price: int):
        self.name = name
''' 

#SET:04
