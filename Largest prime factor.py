from math import sqrt
def isPrime(num):
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True

def primeNumbers(num, start=2):
    for n in range(start, num):
        if isPrime(n):
            yield n

def largestPrimeFactor(num):
    maxPrimeNum = [1]
    primeList = primeNumbers(int(sqrt(num)+1))
    for n in primeList:
        if num % n == 0:
            print(n)
            maxPrimeNum.remove(maxPrimeNum[0])
            maxPrimeNum.append(n)
        if n==num//maxPrimeNum[0]:
            break
    return maxPrimeNum[0]

num=600851475143
#print(largestPrimeFactor(num))

while True:
    for n in range(2, int(sqrt(num) + 1)):
        if num % n == 0:
            num = int(num / n)
            break
    if n == int(sqrt(num)):
        break

print(num)