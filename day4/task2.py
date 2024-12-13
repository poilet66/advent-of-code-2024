with open('day4/input.txt') as file:
    lines = [line.strip() for line in file]

print(len(lines))

solution1 = [['S','.','S'],
             ['']]

def is_xmas(line, point):
    if lines[line][point] != 'X': return False
    if lines