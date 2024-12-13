with open('day6/input.txt') as f:
    lines = [line.strip() for line in f]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

guard_x, guard_y = None, None
for y, line in enumerate(lines):
    if '^' in line:
        guard_x = line.index('^')
        guard_y = y
        break

guard_direction = 0
visited_locs = set([(guard_x, guard_y)])

while True:
    x_off, y_off = directions[guard_direction % len(directions)]
    
    next_x = guard_x + x_off
    next_y = guard_y + y_off
    
    try:
        next_char = lines[next_y][next_x]
    except IndexError:
        break
    
    print(f'Currently at: {(guard_x, guard_y)}')
    
    if next_char == '.':
        guard_x, guard_y = next_x, next_y
        visited_locs.add((guard_x, guard_y))
    elif next_char == '#':
        print('Direction change')
        guard_direction += 1

print(len(visited_locs))


