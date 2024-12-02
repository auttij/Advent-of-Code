times_input = [59, 70, 78, 78]
distances_input = [430, 1218, 1213, 1276]

l = zip(times_input, distances_input)
part_1 = 1
for time, dist in l:
    distances = [t * (time - t) for t in range(time)]
    wins = [d for d in distances if d > dist]
    part_1 *= len(wins)
    

time = int("".join([str(i) for i in times_input]))
dist = int("".join([str(i) for i in distances_input]))

print(time, dist)

def bs(lo, hi, clause):
    while lo <= hi:
        m = (lo + hi) // 2
        if clause(m):
            lo = m + 1
        elif not clause(m):
            hi = m - 1
        else:
            return m
    return m

def search_lo(m):
    return (time - m) * m < dist

def search_hi(m):
    return (time - m) * m > dist

lo = bs(0, time/2, search_lo)
hi = bs(time/2, time, search_hi)
part_2 = hi - lo + 1

print(f"{part_1 = }, {part_2 = }")