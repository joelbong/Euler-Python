from itertools import count

numMax = 20
rangeToDivide = range(numMax-1, 1, -1)

lastNum = 0
for num in count(numMax, numMax):
    for n in rangeToDivide:
        if num % n != 0:
            break
        else:
            lastNum = n
    if lastNum == 2:
        break

print(num)
