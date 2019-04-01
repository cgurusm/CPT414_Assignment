# An algorithm to determine the gcd of two numbers using Consecutive Integer Checking method
# Input: Non negative integers 
# Return Value : absolute/positive integer 
import timeit

# Basic operation
def cic(m,n):
    t = n
    if m < n:
        t = n
    while (t > 1):
        if((m % t == 0) & (n % t == 0)):
            return t
        t = t - 1
    return 1

# Inputing user input
a = int(input("Enter First value: "))
b = int(input("Enter Second value: "))
# Looping through and incrementing inputed values
for i in range(5):
    t  = timeit.Timer(lambda: cic(a, b))
    a = a + 20
    b = b + 20
    print('the GCD values for %s and %s is %s' % (a, b, cic(a,b)))
    print(t.timeit())