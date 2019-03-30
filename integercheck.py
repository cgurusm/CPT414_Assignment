# public class ConsecutiveIntegerChecking {
#   static int GCD(int m, int n) {
#     int t = n;
#     if (m < n)
#       t = m;
#     while (t > 1) {
#       if (m % t == 0 && n % t == 0)
#         return t;
#       t--;
#     }
#     return 1;
#   }
# }





# def gcd(a,b):
#     if (a>b):
#         r1=a
#         r2=b
#     else:
#         r1=b
#         r2=a   
#     if(r1%r2==0):
#         print (r2)
#     else:
#         gcd(r2, r1%r2)
# a= int(input("Enter a number"))
# b= int(input("Enter a number"))
# gcd(a,b)


m = int(input("Enter First value"))
n = int(input("Enter Second value"))
t = min(m, n)
while(t > 0):
    if((m % t == 0) & (n % t == 0)):
        pass
        # return t
    t = t - 1

print(t)