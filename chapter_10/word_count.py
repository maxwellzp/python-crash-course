from pathlib import Path

def count_words(path):
  """Count the approximate number of words in a file."""
  try:
    contents = path.read_text(encoding='utf-8')
  except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
    # pass Failing silently
  else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
  # The file alice.txt has about 29594 words.

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
  path = Path(filename)
  count_words(path)

# The file alice.txt has about 29594 words.
# Sorry, the file siddhartha.txt does not exist.
# The file moby_dick.txt has about 215864 words.
# The file little_women.txt has about 189142 words.
