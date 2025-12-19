from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
# contents = contents.rstrip()
print(contents)
# 3.1415926535
# 8979323846
# 2643383279
