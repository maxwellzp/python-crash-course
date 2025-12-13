favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
  print(f"{name.title()} likes {favorite_languages[name].title()} language.")
# Edward likes Rust language.
# Jen likes Python language.
# Phil likes Python language.
# Sarah likes C language.

