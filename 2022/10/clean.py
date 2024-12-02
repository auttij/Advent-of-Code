def toCmd(input):
    return (
        input[0], 
        int(input[1]) if len(input) > 1 else 0
    )

def updateSignal(cycle, x):
    return (cycle * x) if (cycle % 40) == 20 else 0

def updateCrt(crt, cycle, x):
    c = cycle - 1
    if (c % 40) in [x - 1, x, x + 1]:
        crt[c // 40][c % 40] = '#'

def main(input):
    WIDTH = 40
    cycle = 0
    signal = 0
    x = 1
    crt = [['.' for _ in range(WIDTH)] for _ in range(6)]

    for cmd, amt in map(toCmd, input):
        cycle += 1
        if cmd == 'addx':
            cycle += 1
            signal += updateSignal(cycle - 1, x)
            updateCrt(crt, cycle - 1, x)

        signal += updateSignal(cycle, x)
        updateCrt(crt, cycle, x)
        x += amt

    # output
    print('a', signal)
    for line in crt:
        print("".join(line))

if __name__ == '__main__':
    input = [i.strip().split(' ') for i in open('10/input2.txt').readlines()]
    main(input)
