num = 2*10**6

numberList = range(2, num+1)
endNumber = numberList[-1]
primeList = set()
def sievePrime(numberList):
    primeList.add(numberList[0])
    numberList = [n for n in numberList if n % numberList[0] != 0 and n > numberList[0]]
    if numberList[0]**2 < endNumber:
        sievePrime(numberList)
    else:
        primeList.update(numberList)

    return list(primeList)

print(sum(sievePrime(numberList)))
