def fibo(fibList, n=4*10**6):
    if fibList[-1]<=n:
        fibList.append(fibList[-2]+fibList[-1])
        fibo(fibList, n)
    return(sum(list(filter(lambda x: not x%2, fibList[:-1]))))

fibList = [1,2]
print(fibo(fibList))