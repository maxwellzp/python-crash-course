responses = {}
polling_active = True

while polling_active:
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday? ")

  responses[name] = response

  repeat = input("Would you like to let another person respond? (yes/no) ")
  if repeat == 'no':
    polling_active = False

for name, response in responses.items():
  print(f"{name} would like to climb {response}.")


# What is your name? Maksim
# Which mountain would you like to climb someday? Everest
# Would you like to let another person respond? (yes/no) yes

# What is your name? John
# Which mountain would you like to climb someday? Hoverla
# Would you like to let another person respond? (yes/no) no
# Maksim would like to climb Everest.
# John would like to climb Hoverla.
