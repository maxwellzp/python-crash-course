cities = ['Zaporizhzhia', 'Kharkiv', 'Ternopil', 'Chernigiv']
cities.sort()
print(cities)
# ['Chernigiv', 'Kharkiv', 'Ternopil', 'Zaporizhzhia']

cities = ['Zaporizhzhia', 'Kharkiv', 'Ternopil', 'Chernigiv']
cities.sort(reverse=True)
print(cities)
# ['Zaporizhzhia', 'Ternopil', 'Kharkiv', 'Chernigiv']

cities = ['Zaporizhzhia', 'Kharkiv', 'Ternopil', 'Chernigiv']
print("Here is the original list:")
print(cities)

print("\nHere is the sorted list:")
print(sorted(cities))

print("\nHere is the oroginal list again:")
print(cities)

# printing a list in reverse order
cities.reverse()
print(cities)

# finding the length of a list
print("the cities list has:", len(cities), "items")

