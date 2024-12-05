with open('day4/input.txt') as file:
    lines = [line.strip() for line in file]

print(len(lines))

letters = ['X', 'M', 'A', 'S']

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
    'NW': (-1, -1),
    'NE': (-1, 1),
    'SW': (1, -1),
    'SE': (1, 1)
}

def check_pos(line, position, letterIndex, direction):
    if line < 0 or line >= len(lines) or position < 0 or position >= len(lines[0]): return 0
    if lines[line][position] != letters[letterIndex]: return 0
    if letterIndex == 3: return 1
    else:
        letterIndex += 1
        return check_pos(line + directions.get(direction)[0], position + directions.get(direction)[1], letterIndex, direction)

sum = 0
for line_num, line in enumerate(lines):
    for pos, _ in enumerate(line):
        for direction in directions.keys():
            sum += check_pos(line_num, pos, 0, direction)

print(sum)


