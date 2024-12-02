instrs = [l.strip().replace(':', '=') for l in open('21/input2.txt', 'r')]
root = None
while root is None:
    for l in instrs:
        try:
            exec(l)
        except NameError:
            pass
print(root)