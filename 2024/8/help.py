import fileinput, itertools

a, w, h = {}, 0, 0
for y, r in enumerate(open("input2.txt").read().strip().split("\n")):
    for x, c in enumerate(r.strip("\n")):
        if c != ".":
            a.setdefault(c, []).append((x, y))
        w, h = max(w, x + 1), max(h, y + 1)

n1, n2 = set(), set()
for f, p in a.items():
    for i, j in itertools.combinations(p, 2):
        dx, dy = j[0] - i[0], j[1] - i[1]
        x, y, s = *j, 0
        while 0 <= x < w and 0 <= y < h:
            if s == 1:
                n1.add((x, y))
            n2.add((x, y))
            x, y, s = x + dx, y + dy, s + 1
        x, y, s = *i, 0
        while 0 <= x < w and 0 <= y < h:
            if s == 1:
                n1.add((x, y))
            n2.add((x, y))
            x, y, s = x - dx, y - dy, s + 1
print(len(n1), len(n2))
