data_pth = '/Users/ondrejleder/git_repos/advent_of_code_2021/data/input_3_1.txt'

with open(data_pth, 'r') as in_file:
    data = in_file.readlines()
    data = [line.rstrip() for line in data]


def filter_to_last(values, most=True, ind=0):
    ones = []
    zeros = []

    for value in values:
        if value[ind] == '1':
            ones.append(value)
        else:
            zeros.append(value)
    zl = len(zeros)
    ol = len(ones)

    if most:
        if zl > ol:
            out = zeros
        else:
            out = ones

    else:
        if ol < zl:
            out = ones
        else:
            out = zeros

    if len(out) == 1:
        return out
    else:
        return filter_to_last(out, most=most, ind=ind + 1)


print(int(filter_to_last(data, most=False, ind=0)[0], 2)*int(filter_to_last(data, most=True, ind=0)[0], 2))
