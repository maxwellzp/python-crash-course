print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
  first_number = input("\nFirst number: ")
  if first_number == 'q':
    break
  second_number = input("Second number: ")
  if second_number == 'q':
    break
  try:
      answer = int(first_number) / int(second_number)
  except ZeroDivisionError:
     print("You can't divide by 0!")
  else:
     print(answer)

# Give me two numbers, and I'll divide them.
# Enter 'q' to quit.

# First number: 10
# Second number: 5
# 2.0

# First number: 12
# Second number: 5
# 2.4
