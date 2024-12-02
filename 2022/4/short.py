import re

gen = (
    map(int, re.findall(r'\d+', line))
    for line in open("4/input2.txt").readlines()
)

a, b = 0, 0
for s1, e1, s2, e2 in gen:
    # (s1, e1) contains (s2, e2) if both ends are contained within the first range
    #    s2 -- e2
    # s1 -- -- e1
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        a += 1

    # (s2,e2) overlaps (s1,e1) if it is not completely to the left or completely to the right
    #        s2 -- e1
    #  s1 -- -- e1
    if not (e1 < s2 or s1 > e2):
        b += 1
print(a, b)
