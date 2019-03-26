from math import sqrt

# Second implementation
sumNumbers = 1000
numberOfNumbers = 3
for a in range(round(sqrt(sumNumbers)), sumNumbers//numberOfNumbers):
    b = round((1000-2*a)/(1000-a)*500)
    c = sumNumbers - a - b
    if a < b and (a**2+b**2) == c**2:
        print(a, b, c)
        print(a*b*c)
        break
exit()
# first implementation, no result
numMax = 1000

for num1 in range(numMax):
    for num2 in range(numMax):
        num3 = sqrt(num1**2 + (num2+1)**2)
        if num1 < num2 and float(num3).is_integer() and (num1+num2+int(num3))<=1000:
            print(num1, num2, int(num3), (num1+num2+int(num3)))

