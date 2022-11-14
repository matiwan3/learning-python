class Warehouse:
    purpose = 'storage'
    region = 'west'
    
w1 = Warehouse()
print(Warehouse.purpose, Warehouse.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)