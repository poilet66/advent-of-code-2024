
with open('day1/input.txt') as f:
    pairs = [line.strip().split('   ') for line in f]
    left, right = zip(*pairs)
    

right_occurences = {x : right.count(x) for x in left }

print(sum(int(x) * int(y) for x,y in right_occurences.items()))
