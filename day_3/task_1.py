data_pth = '/Users/ondrejleder/git_repos/advent_of_code_2021/data/input_3_1.txt'


with open(data_pth, 'r') as in_file:
    data = in_file.readlines()
    data = [line.rstrip() for line in data]

one_counts = {}

for ind, char in enumerate(data[0]):
    one_counts[ind] = 0


for row in data:
    for ind, char in enumerate(row):
        one_counts[ind] += int(char)

gamma = ''
epsilon = ''

for ind in range(len(data[0])):
    if one_counts[ind] > len(data)//2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
