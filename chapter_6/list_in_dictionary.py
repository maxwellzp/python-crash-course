pizza = {
  'crust': 'thick',
  'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza " 
      "with the following toppings:")

for topping in pizza['toppings']:
  print(f"\t{topping}")

# You ordered a thick-crust pizza with the following toppings:
# 	mushrooms
# 	extra cheese

