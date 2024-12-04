from typing import List

def all_same(input: List[int]) -> bool:
    op = 'less' if input[0] < input[1] else 'more'
    for i in range(1, len(input) - 1):
        if op == 'less':
            if int(input[i]) > int(input[i + 1]): return False
        else:
            if int(input[i]) < int(input[i + 1]): return False
    return True

def dont_differ(input: List[int]) -> bool:
    for i in range(0, len(input) - 1):
        diff = abs(input[i] - input[i + 1])
        if diff < 1 or diff > 3: return False
    return True

list_nums = '1 4 5 6 9'
nums = list(map(int, list_nums.split(' ')))

with open('day2/input.txt') as f:
    lines = [list(map(int, line.strip().split(' '))) for line in f]


safe = 0
for line in lines:
    if all_same(line) and dont_differ(line): safe += 1

print(safe)