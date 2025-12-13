alien = {'color': 'green'}
print(f"The alien is {alien['color']}.")
# The alien is green.

alien['color'] = 'yellow'
print(f"The alien is now {alien['color']}.")
# The alien is now yellow.

alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien['x_position']}")
# Original position: 0

if alien['speed'] == 'slow':
  x_increment = 1
elif alien['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

alien['x_position'] = alien['x_position'] + x_increment

print(f"New position: {alien['x_position']}")
# New position: 2

