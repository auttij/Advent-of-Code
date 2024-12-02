from random import randint

def write(data):
    with open('4/input3.txt', 'w') as f:
        f.writelines(data)

def create():
    sectionMin, sectionMax = 1, 200
    areaMin, areaMax = 1, 100
    groupCount = 2000
    groupMin, groupMax = 2, 5
    
    output = []
    for group in range(groupCount):
        groupSize = randint(groupMin, groupMax)
        elves = []
        for _ in range(groupSize):
            areaSize = randint(areaMin, areaMax)
            sectionMaxStart = sectionMax - areaSize
            areaStart = randint(sectionMin, sectionMaxStart)
            elves.append(f"{areaStart}-{areaStart + areaSize}")
        line = ",".join(elves)
        output.append(line)
    write("\n".join(output))


if __name__ == "__main__":
    create()