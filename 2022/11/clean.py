from collections import defaultdict
import os
import copy

def parse():
    lineNum = 0
    inventories = []
    operations = []
    tests = []
    targets = []

    with open("11/input2.txt", "r") as data:
        for t in data:
            line = t.strip()
            if lineNum % 7 == 1:
                _, A = line.split(": ")
                nums = list(map(int, A.split(", ")))
                inventories.append(nums)
            elif lineNum % 7 == 2:
                _, A = line.split("= ")
                newTuple = tuple(A.split())
                operations.append(newTuple)
            elif lineNum % 7 == 3:
                _, A = line.split("by ")
                tests.append(int(A))
            elif lineNum % 7 == 4:
                _, A = line.split("ey ")
                targetList = [int(A)]
            elif lineNum % 7 == 5:
                _, A = line.split("ey ")
                targetList.append(int(A))
                newTuple = tuple(targetList)
                targets.append(newTuple)
            lineNum += 1
    return inventories, operations, tests, targets
    
def countNewVal(m, inventories, operations, superModulo, part):
    currentItem = inventories[m].pop(0)
    A, B, C = operations[m]
    if B == "+":
        currentItem += int(C)
    if B == "*":
        if C == "old":
            currentItem *= currentItem
        else:
            currentItem *= int(C)
    if part == 1:
        currentItem = currentItem // 3
    else:
        currentItem = currentItem % superModulo
    return currentItem

def throw(m, currentItem, inventories, targets, tests):
    T, F = targets[m]
    if currentItem % tests[m] == 0:
        inventories[T].append(currentItem)
    else:
        inventories[F].append(currentItem)

def main():
    throwCounts = defaultdict()
    inventories, operations, tests, targets = parse()

    originalInventories = copy.deepcopy(inventories)
    answers = []
    superModulo = 1
    for t in tests:
        superModulo *= t

    for part in [1,2]:
        for t in range(8):
            throwCounts[t] = 0
        if part == 2:
            inventories = copy.deepcopy(originalInventories)
            rounds = 10000
        else:
            rounds = 20

        for r in range(rounds):
            if r % 100 == 0:
                print(r, end='\r')
            # print(r, MonkeyThrowCounts)
            for m in range(8):
                while inventories[m]:
                    item = countNewVal(m, inventories, operations, superModulo, part)
                    throw(m, item, inventories, targets, tests)
                    throwCounts[m] += 1
        
        throwList = throwCounts.values()  
        throwList = sorted(throwList, reverse=True)[:2] 
        answer = throwList[0] * throwList[1]
        answers.append(answer)
        
    a, b = answers
    print(f"{a = }")
    print(f"{b = }")

if __name__ == '__main__':
    main()