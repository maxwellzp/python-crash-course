from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
  print(line)
# 3.1415926535
# 8979323846
# 2643383279
