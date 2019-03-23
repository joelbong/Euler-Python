from itertools import count

def isPrime(num):
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True

stop = 10001
start = 0
for n in count(2):
    if isPrime(n):
        print(n)
        start += 1
        if start == stop:
            primeNumber = n
            break

print(primeNumber)