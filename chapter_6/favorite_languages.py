favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python'
}

print(favorite_languages)
# {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# Sarah's favorite language is C.

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")
# Sarah's favorite language is C.
# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Rust.
# Phil's favorite language is Python.

# Looping through all the keys in a dictionary
for name in favorite_languages.keys():
  print(name.title())
# Jen
# Sarah
# Edward
# Phil

if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")


