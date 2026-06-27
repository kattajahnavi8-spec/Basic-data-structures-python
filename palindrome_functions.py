def palindrome(n):
    return n==int(str(n)[::-1])
print(palindrome(121))