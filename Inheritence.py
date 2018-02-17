import string
import random
import numpy as np
import pandas as pd
import json

class codes(object):
   
    Id =""
    name =""
    quantity=""
    price=""
    origin=""
    destination =""
    
    def __init__(self, Id, name, quantity, price, origin, destination):
        
        self.Id = Id
        self.name = name # name of the product 
        self.quantity = quantity # Quantity in Kgs
        self.price = quantity # in Rupees
        self.origin = origin # Origin from where the produce starts
        self.detination = destination # Destination of the product.
    
if __name__ == '__main__':
  
   
    Id = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range (8))
    a = str(input("Enter the name: "))
    b = int(input("Enter the quantity in Kgs: "))
    c = int(input("Enter the price in INR: "))
    d = str(input("Enter the Origin: "))
    e = str(input("Enter the Destination: "))
    
    Entry = codes(Id, a, b, c, d, e)
      
        #convert records elements into json
    jsondata = json.dumps(Entry.__dict__)
    print("The following objects are serialized:", jsondata)
    