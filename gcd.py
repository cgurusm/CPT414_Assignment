# An algorithm to determine the gcd of two numbers using Euclid algorithm
# Input: Non negative integers 
# Return Value : absolute/positive integer 

# import math 
import time



# m = input("Enter first value: ")
# n = input("Enter Second value: ")
# # for r in m: 
# #     m++
# print ("The gcd of {} and {} is : ".format(m,n))
# start = time.time()
# print (math.gcd(int(m), int(n))) 

# end = time.time()
# print(end)


def GCD(m, n): 
  
   while(n): 
       m, n = n, m % n 
   return m 
  
a = input("Enter first value: ")
b= input("Enter first value: ")

start = time.time()
g = GCD(int(a),int(b))  
end = time.time() 

print ("The gcd of {} and {} is : {} ".format(a,b,g)) 
print(end)
 