dimensions = (200, 50)
print(dimensions[0]) #200
print(dimensions[1]) #50


# dimensions[0] = 100
# TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:
  print("=>", dimension)
# => 200
# => 50

# redefine the dimensions tuple
dimensions = (400, 100)
for dimension in dimensions:
  print("new tuple", dimension)
# new tuple 400
# new tuple 100

