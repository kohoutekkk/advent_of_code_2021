data_pth = '/Users/ondrejleder/git_repos/advent_of_code_2021/data/input_2_1.txt'

with open(data_pth, 'r') as in_file:
    data = in_file.readlines()
    data = [line.rstrip() for line in data]

horizontal = 0
vertical = 0
aim = 0

for obs in data:
    direction, value = obs.split(' ')
    value = int(value)

    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    elif direction == 'forward':
        horizontal += value
        vertical += (value * aim)

print(horizontal * vertical)