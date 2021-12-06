data_pth = '/Users/ondrejleder/git_repos/advent_of_code_2021/data/input_2_1.txt'

with open(data_pth, 'r') as in_file:
    data = in_file.readlines()
    data = [line.rstrip() for line in data]

horizontal = 0
vertical = 0

for obs in data:
    direction, value = obs.split(' ')
    value = int(value)
    #print(direction)
    #print(value)

    if direction == 'forward':
        horizontal += value
    elif direction == 'down':
        vertical += value
    elif direction == 'up':
        vertical -= value

    #print(horizontal)
    #print(vertical)
    #print('-'*10)

print(horizontal * vertical)