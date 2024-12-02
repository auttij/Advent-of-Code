lines = [tuple(map(int, i.split())) for i in open("input2.txt", "r").readlines()]

# separate columns to their own sorted lists
l1, l2 = list(map(sorted, zip(*lines)))

# part 1
part_1 = sum([max(pair) - min(pair) for pair in zip(l1, l2)])

# part 2
from collections import Counter

counts = Counter(l2)
part_2 = sum([i * counts[i] if i in counts else 0 for i in l1])

# out
print(f"{part_1 = }")
print(f"{part_2 = }")
