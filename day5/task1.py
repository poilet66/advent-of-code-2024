with open('day5/input.txt') as f:
    text = f.read()

    rules = text.split('\n\n')[0].split('\n')
    actions = text.split('\n\n')[1].split('\n')

print(actions)

rules_dict = {}

# Map number to all numbers it must come before
for rule in rules:
    left = int(rule.split('|')[0])
    right = int(rule.split('|')[1])
    if rules_dict.get(left) is None:
        rules_dict[left] = [right]
    else:
        rules_dict.get(left).append(right)

valid_prints = []

for action in actions:
    pages = action.split(',')
    valid = True
    for idx, current_page in enumerate(pages):
        # iterate through list, check if any of preceeding numbers after should have came first
        for other_num in pages[idx+1:]:
            if current_page in rules_dict.get(other_num, []): 
                valid = False
                break
        if not valid: break
    if valid:
        valid_prints.append(action)
        
# sum middle value of valid
print(sum([int(my_list[len(my_list)//2]) for my_list in valid_prints]))
