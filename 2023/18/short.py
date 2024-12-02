with open('input2.txt', 'r') as f:
    data = [line.strip().split(" ") for line in f.readlines()]
in1 = [(d, int(n)) for d, n, c in data]

dirs= { '0': 'R', '1': 'D', '2': 'L', '3': 'U' }
in2 = [(dirs[c[-2]], int(c[2:-2], 16)) for d, n, c in data]


tr = { "R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
for p in [("part 1", in1), ("part 2", in2)]:
    part, input = p

    area = 0
    perimeter = 0
    y, x = 0, 0
    for d, length in input:
        dy, dx = tr[d]
        dy, dx = dy*length, dx*length
        y, x = y+dy, x+dx
        perimeter += length
        area += x*dy

    print(f"{part}: {area + perimeter//2 + 1}") 
