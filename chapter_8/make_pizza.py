def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# Making a pizza with the following toppings:
# - pepperoni

# Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
