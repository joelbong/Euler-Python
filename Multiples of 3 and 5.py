result = sum([num for num in range(1000) if divmod(num, 3)[1]==0 or divmod(num,5)[1]==0])
print(result)