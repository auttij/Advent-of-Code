line = open('6/input2.txt').read().strip()

def test(size, i):
    return len(set(line[i-size:i])) == size

def f(size):
    return [test(size, i) for i in range(len(line))].index(True)

print(f"a: {f(4)}, b: {f(14)}")
