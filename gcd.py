# An algorithm to determine the gcd of two numbers using Euclid algorithm
# Input: Non negative integers 
# Return Value : absolute/positive integer 
import timeit

def GCD(m, n): 
  
   while(n): 
       m, n = n, m % n 
   return m 
  
a = int(input("Enter First value: "))
b = int(input("Enter Second value: "))
for i in range(20):
    t  = timeit.Timer(lambda: GCD(a, b))
    a = a + 20
    b = b + 20
    print('the GCD values for %s and %s is %s' % (a, b, GCD(a,b)))
    print(t.timeit())