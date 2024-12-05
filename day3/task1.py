import re

with open('day3/input.txt') as f:
    lines = f.read()

pattern = r'mul\(\d+,\d+\)'

matches = re.findall(pattern, lines)

print(len(matches))

pattern = r'\d+'
sum = 0
for mult in matches:
    matches = re.findall(pattern, mult)
    left = matches[0]
    right = matches[1]
    sum += int(left) * int(right)
print(sum)