aliens = []

for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
  print(alien)
print('...')
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...

print(f"Total number of aliens: {len(aliens)}")
# Total number of aliens: 30

