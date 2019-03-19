minNum = 100
maxNum = 999

def isPalindrome(num):
    reverseNum = ''
    for l in range(len(str(num))-1, -1, -1):
        reverseNum+=str(num)[l]
    if str(num) == reverseNum:
        return True
    else:
        return False

for num in range(maxNum**2, minNum**2, -1):
    stop = False
    if isPalindrome(num):
        for n in range(minNum, maxNum):
            if num % n == 0 and len(str(num//n))==3:
                palindrome = num
                number1, number2 = n, num//n
                stop = True
                break
    if stop == True:
        break

print(palindrome, number1, number2)

#could also use isPrime false instead of second if.
