vehicles = ['bus', 'car', 'train', 'plane', 'bike']
vehicles_2 = vehicles[:]

print("First list: ")
print(vehicles)
print("Second list:")
print(vehicles_2)
# First list: 
# ['bus', 'car', 'train', 'plane', 'bike']
# Second list:
# ['bus', 'car', 'train', 'plane', 'bike']

vehicles.append("tram")
vehicles_2.append("scooter")

print("First list: ")
print(vehicles)
print("Second list:")
print(vehicles_2)
# First list: 
# ['bus', 'car', 'train', 'plane', 'bike', 'tram']
# Second list:
# ['bus', 'car', 'train', 'plane', 'bike', 'scooter']



