num = 100
numList = range(num+1)
difference = sum(numList)**2 - sum(map(lambda x: x**2, numList))
print(difference)