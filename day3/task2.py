import re

def extract_output(input: str) -> int:
    pattern = r'\d+'
    matches = re.findall(pattern, input)
    return int(matches[0]) * int(matches[1])

with open('day3/input.txt') as f:
    lines = f.read()

# match groups
pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'


sum = 0
mult_next = True
for found in re.finditer(pattern, lines):
    string = found.group()
    if "don't" in string:
        mult_next = False
    elif "do" in string:
        mult_next = True
    elif "mul" in string and mult_next:
        sum += extract_output(string)

print(sum)