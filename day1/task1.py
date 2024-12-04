from typing import List
import os

print(os.path.exists('day1/input.txt'))


with open('day1/input.txt') as file:
    pairs = [line.strip().split('   ') for line in file]
    print(pairs[0])
    left, right = zip(*pairs)

left = sorted(map(int, left))
right = sorted(map(int, right))

sum = 0

for i in range(len(left)):
    sum += abs(int(left[i]) - int(right[i]))

print(sum)

