lines = open("3/input2.txt").read().strip().split("\n")
l = iter(lines)

def priority(c):
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

def intersect(*ls):
    return next(iter(set.intersection(*map(set, ls))))

def err(line):
    f, s = line[:len(line)//2], line[len(line)//2:]
    return priority(intersect(f, s))

a = sum(list(map(err, lines)))
b = sum([priority(intersect(l1, l2, l3)) for l1, l2, l3 in zip(l, l, l)])
print(a, b)