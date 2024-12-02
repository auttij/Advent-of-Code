with open('input2.txt') as f:
    data = f.readlines()
lines = [line.strip() for line in data]

p1, p2 = 0, 0
for line in lines:
    p1_digits = []
    p2_digits = []

    for i, c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)

        for d, num in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(num):
                p2_digits.append(str(d))

    p1 += int(f"{p1_digits[0]}{p1_digits[-1]}")
    p2 += int(f"{p2_digits[0]}{p2_digits[-1]}")

print(f"{p1 = }")
print(f"{p2 = }")
    
