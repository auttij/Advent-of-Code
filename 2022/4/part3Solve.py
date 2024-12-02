lines = open('4/input3.txt').read().split("\n")

# read input
arr = []
for line in lines:
    group = line.split(',')
    arr.append([list(map(int, area.split('-'))) for area in group])

# solve
count = 0
for i, group in enumerate(arr):
    ranges = [set(range(a, b + 1)) for a, b in group]
    if len(set.intersection(*ranges)):
        count += 1
print(count)
