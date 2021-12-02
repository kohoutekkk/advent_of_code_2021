data_pth = '/Users/ondrejleder/git_repos/advent_of_code_2021/data/input_1_1.txt'

with open(data_pth, 'r') as in_file:
    data = in_file.readlines()
    data = [int(line.rstrip()) for line in data]

total_down = 0

#pick a starting point at the end of the second sequence and enum, that will
# take the proper number for the first sequence
for ind, number in enumerate(data[3:]):
    #i want to compare sums of those two lists, that means i only need to compare i-1 and i+2
    #a = [data[i-1], data[i], data[i+1]]
    #b = [data[i], data[i+1], data[i+2]]
    if number > data[ind]:
        total_down += 1

print(total_down)
