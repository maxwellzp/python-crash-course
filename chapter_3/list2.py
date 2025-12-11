animals = ['cat', 'dog', 'tiger']
print(animals)

animals[0] = 'fox'
print(animals)

# add a new element to the list
animals.append('lion')
print(animals)

birds = []
birds.append('owl')
birds.append('crow')
birds.append('stork')
print(birds)

birds.insert(0, 'sparrow')
print(birds)

# removing an item from the list
del birds[0]
print(birds)

# removing an item using pop() method
popped_bird = birds.pop()
print("popped_bird: ", popped_bird)
print(birds)

# popping items from any position in the list
first_bird = birds.pop(0)
print(first_bird)

# removing an item by value
birds.remove('crow')
print(birds)

