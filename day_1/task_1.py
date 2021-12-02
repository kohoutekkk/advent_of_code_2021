
data_pth = '/Users/ondrejleder/git_repos/advent_of_code_2021/data/input_1_1.txt'

with open(data_pth, 'r') as in_file:
    data = in_file.readlines()
    data = [int(line.rstrip()) for line in data]

current = data[-5]
total_down = 0
print(current)

for next_depth in data:

    if next_depth > current:
        total_down += 1
    current = next_depth

print(total_down)

