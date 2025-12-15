prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I'd love to go to {city.title()}!")


# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.)Lviv
# I'd love to go to Lviv!

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.)Kyiv
# I'd love to go to Kyiv!

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.)quit
